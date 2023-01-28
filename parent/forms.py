from django.forms import ModelForm, TextInput,ClearableFileInput,DateInput,Select,EmailInput,NumberInput
from .models import Parent, Location
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.utils.translation import gettext as _
class ParentForm(ModelForm):
    class Meta:
        model = Parent
        exclude = ['parent_address','added_by']
        widgets = {
            'parent_name': TextInput(attrs={'class': 'form-control'}),
            'parent_photo': ClearableFileInput(attrs={'class': 'form-control', 'accept': '.png, .jpg'}),
            'parent_date_of_birth': DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'parent_place_of_birth': TextInput(attrs={'class': 'form-control'}),
            'parent_gender': Select(attrs={'class': 'form-control'}),
            'id_type': Select(attrs={'class': 'form-control'}),
            'id_file': ClearableFileInput(attrs={'class': 'form-control'}),
            'parent_phone_no': TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "parent_photo": _('photo'),
            "parent_name":  _('name'),
            "parent_gender":  _('gender'),
            "id_type":  _('id type'),
            "id_file":  _('id file'),
            "parent_phone_no":  _('phone number'),
            "parent_address":  _('address'),
        }


class ParentAddressForm(ModelForm):
    class Meta:
        model = Location
        fields = ('governorate', 'district')
        widgets = {
            'governorate': Select(attrs={'class': 'form-control'}),
            'district': Select(attrs={'class': 'form-control'}),
        }
