
import pandas as pd
import numpy as np
from pandas import Timestamp
from collections import defaultdict
from datetime import datetime, date, timedelta
import json
from django.db.models.fields import (BigAutoField, BooleanField, CharField, DateField, DateTimeField, 
    FloatField, TextField, IntegerField, DecimalField, PositiveSmallIntegerField, PositiveIntegerField, PositiveBigIntegerField
)
from django.db.models.fields.related import ForeignKey, ManyToManyField


from django.apps import apps
from django.core.management import BaseCommand
from django.db import transaction

class Command(BaseCommand):
    """
    Populate database from Excel file.

    Excel file should be correctly formatted:
    - One sheet per model, bearing the name of the model (e.g. Auth.User)
    - In each sheet, a table with fields named exactly as they are in the model
    - If -a/--app is specified (e.g. -a auth), this will be used as the model's app name (and the output filename).
      If not, then it's assumed that the sheet name contains the model's app name (e.g. "auth.Group")
    """

    help = "DEV COMMAND: Populate database from Excel"

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('-f', '--from', type=str, help='Path to Excel file')
        parser.add_argument('-a', '--app', type=str, help='App')

    def handle(self, *args, **options):
        if not (options['from']):
            print('Usage: python manage.py data_from_excel --from emis/fixtures/fixtures.xlsx --app emis')
            return

        self.generate(options['from'], options['app'])

    @transaction.atomic
    def generate(self, fixture_file, app):
        print(f'Reading {fixture_file}... ')
        xls = pd.ExcelFile(fixture_file, engine='openpyxl')
        for sheet in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=sheet)
            df = df.replace({np.nan: None})
            model, col_types = self.get_column_types(sheet, df, app)
            model_name = model._meta.model_name
            print(f'Inserting into {model_name}... ', end="", flush=True)
            instances = []
            m2m_instances = defaultdict(list)
            id_specified = 'id' in col_types
            for row in df.itertuples():
                args = {}
                row_dict = row._asdict()
                for field, value in row_dict.items():
                    if field not in col_types and field[-3:] == '_id':
                        field = field[:-3] # remove _id suffix
                    if field == 'Index':
                        if not id_specified: args['id'] = value
                        continue
                    if col_types[field]['type'] == 'm2m':
                        values = json.loads(value)
                        linked_model = col_types[field]['django_field'].related_model
                        m2m_model = getattr(model, field).through
                        for val in values:
                            m2m_args = {f'{model_name}_id': row_dict.get('id', row_dict['Index']), f'{linked_model._meta.model_name}_id': val}
                            m2m_instance = m2m_model(**m2m_args)
                            m2m_instances[m2m_model].append(m2m_instance)
                        continue
                    try:
                        dest_field = field
                        if col_types[field]['type'] == 'fk':
                            dest_field = f'{dest_field}_id'
                        if value is None: continue
                        args[dest_field] = convert_value(value, col_types[field]['python_type'])
                    except Exception as e:
                        print(f'Warning: Could not convert {value} to {col_types[field]["python_type"]}. Defaulting to None ({e})')
                        args[field] = None
                instances.append(model(**args))
            model.objects.bulk_create(instances)
            for model, m2m_objs in m2m_instances.items():
                m2m_model.objects.bulk_create(m2m_objs)
            print('Done')

    def get_column_types(self, sheet_name, df, app=None):
        col_types = {}
        model_name = sheet_name
        if app: model_name = f'{app}.{sheet_name}'
        model = apps.get_model(model_name)
        for col in df.columns:
            try:
                field = model._meta.get_field(col)
                col_types[field.name] = field_to_python_type(field)
                col_types[field.name]['django_field'] = field
            except Exception as e:
                print(f'Error: {e}')
                return
        return model, col_types

int_fields = (BigAutoField, IntegerField, PositiveSmallIntegerField, PositiveIntegerField, PositiveBigIntegerField,)
def field_to_python_type(field, type = None):
    python_type = None
    type_str = None
    if isinstance(field, CharField) or isinstance(field, TextField):
        type_str, python_type = 'str', str
    elif any([isinstance(field, int_field) for int_field in int_fields]):
        type_str, python_type = 'int', int
    elif isinstance(field, ForeignKey):
        return field_to_python_type(field.related_model._meta.pk, 'fk')
    elif isinstance(field, DecimalField) or isinstance(field, FloatField):
        type_str, python_type = 'float', float
    elif isinstance(field, DateTimeField): type_str, python_type = 'datetime', datetime
    elif isinstance(field, DateField): type_str, python_type = 'date', date
    elif isinstance(field, BooleanField): type_str, python_type = 'bool', bool
    elif isinstance(field, ManyToManyField): type_str, python_type = 'm2m', list
    else:
        print('Field type for {} not implemented'.format(field))
    return {'type': type or type_str, 'python_type': python_type}

def convert_value(value, python_type):
    if value is None:
        return None
    if (python_type is datetime or python_type is date) and type(value) is Timestamp:
        return value.to_pydatetime()
    if type(value) == python_type:
        return value
    if type(value) is float and python_type is str:
        return str(int(value))
    return python_type(value)
    
