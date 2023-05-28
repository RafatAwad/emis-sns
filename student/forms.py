from django.forms import ModelForm,Select,TextInput,ClearableFileInput,DateInput,ModelChoiceField,IntegerField,NumberInput,Form,BooleanField,FileInput,CheckboxInput,SelectMultiple,Textarea
from .models import Location, School, Document, StudentInfo, P_p
from address.models import Location
from django.utils.translation import gettext as _


class StudentAddressForm2(ModelForm):
    class Meta:
        model = Location
        fields = ['governorate']
        exclude =[]
        widgets = {
            'governorate': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            "governorate": _('governorate'),
        }
class ParentAddressForm(ModelForm):
    class Meta:
        model = Location
        fields = ['governorate']
        exclude =[]
        widgets = {
            'governorate': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            "governorate": _('governorate'),
        }
class StudentAddressForm(ModelForm):
    class Meta:
        model = Location
        fields = ['governorate', 'district', 'sub_district', 'village', 'sub_village']
        exclude =[]
        widgets = {
            'governorate': Select(attrs={'class': 'form-control'}),
            'district': Select(attrs={'class': 'form-control'}),
            'sub_district': Select(attrs={'class': 'form-control'}),
            'village': Select(attrs={'class': 'form-control'}),
            'sub_village': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            "governorate": _('governorate'),
            "district":  _('district'),
            "sub_district":  _('sub district'),
            "village":  _('village'),
            "sub_village":  _('sub village'),
        }
class  StudentForm(ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        exclude = ['emis_id','added_date','added_by','checked','documents','parent','address','school','checked_by','checked_date','year']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'photo': ClearableFileInput(attrs={'class': 'form-control', 'accept': '.png, .jpg'}),
            'date_of_birth': DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'place_of_birth': TextInput(attrs={'class': 'form-control'}),
            'disease': TextInput(attrs={'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-control'}),
            'spn_type': Select(attrs={'class': 'form-control'}),
            'shift': Select(attrs={'class': 'form-control'}),
            'grade': Select(attrs={'class': 'form-control'}),
            'ur_or_ru': Select(attrs={'class': 'form-control'}),
            'relation': Select(attrs={'class': 'form-control'}),
            'father_job': TextInput(attrs={'class': 'form-control'}),
            'mother_name': TextInput(attrs={'class': 'form-control'}),
            'mother_work': TextInput(attrs={'class': 'form-control'}),
            'family_status': Select(attrs={'class': 'form-control'}),
            'live_with': Select(attrs={'class': 'form-control'}),
            'socit': Select(attrs={'class': 'form-control'}),
            'edu_status': CheckboxInput(attrs={'class': 'form-control'}),
            'skills': TextInput(attrs={'class': 'form-control'}),
            'note': Textarea(attrs={'class': 'form-control', 'rows':'3'}),
            
        }
        labels = {
            "gender": _('gender'),
            "shift":  _('shift'),
            "spn_type":  _('Type of Disability'),
            "relation":  _('relation'),
            "school":  _('school'),
            "grade":  _('grade'),
            "socit":  _('type of society'),
            "live_with":  _('live with'),
            "ur_or_ru":  _('rural or unrural'),
            "skills":  'المهارات التي يمتلكها الطالب ؟',
            "edu_status": 'هل الطالب منقطع عن الدراسة ؟',
            "family_status": _('family status'),
        }


class ChechForm(Form):
    class Meta:
        model = StudentInfo
        fields = ['checked']

class StudentSchoolForm(ModelForm):
    class Meta:
        model = School
        exclude =['school_address','school_code']
        widgets = {
            'school_name': TextInput(attrs={'class': 'form-control' }),
            'school_phone_no': TextInput(attrs={'class': 'form-control' }),
            'school_address': Select(attrs={'class': 'form-control' }),
            'school_shift': Select(attrs={'class': 'form-control' }),
            'school_levels': SelectMultiple(attrs={'class': 'form-control' }),
        }
        labels = {
            "school_name": _('name'),
            "school_phone_no": _('phone number'),
            "school_address": _('address'),
            "school_gender":  _('school gender'),
            "school_shift":  _('shift'),
            "school_levels":  _('levels'),
        }

class StudentParentForm(ModelForm):
    class Meta:
        model = P_p
        fields = '__all__'
        exclude =['parent_address','added_by']
        widgets = {
            'parent_name': TextInput(attrs={'class': 'form-control'}),
            'parent_photo': ClearableFileInput(attrs={'class': 'form-control'}),
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
        fields = ['governorate', 'district']
        exclude =[]
        widgets = {
            'governorate': Select(attrs={'class': 'form-control', 'id': 'parent_governorate'}),
            'district': Select(attrs={'class': 'form-control','id':'parent_district'}),
        }
        labels = {
            "governorate": _('governorate'),
            "district":  _('district'),
        }
class StudentDocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
