from django.forms import ModelForm,Select,TextInput,SelectMultiple,DateInput,ModelMultipleChoiceField,CheckboxSelectMultiple
from .models import Teachers,ObjectsL,TeachQual,Grade
from address.models import Location
from django.utils.translation import gettext as _


class TeacherstAddressForm2(ModelForm):
    class Meta:
        model = Location
        fields = ['governorate']
        widgets = {
            'governorate': Select(attrs={'class': 'form-control'}),
        }
        labels = {
            "governorate": _('governorate'),
        }

class TeacherstAddressForm(ModelForm):
    class Meta:
        model = Location
        fields = ['governorate', 'district', 'sub_district', 'village', 'sub_village']
        widgets = {
            'governorate': Select(attrs={'class': 'form-control'}),
            'district': Select(attrs={'class': 'form-control'}),
            'sub_district': Select(attrs={'class': 'form-control'}),
            'village': Select(attrs={'class': 'form-control'}),
            'sub_village': Select(attrs={'class': 'form-control'})
        }
        labels = {
            "governorate": _('governorate'),
            "district":  _('district'),
            "sub_district":  _('sub district'),
            "village":  _('village'),
            "sub_village":  _('sub village'),
        }
class  TeachersForm(ModelForm):
    class Meta:
        model = Teachers
        fields = '__all__'
        exclude =['teacher_address','teacher_school','added_by']
        widgets = {
            'job_code': TextInput(attrs={'class': 'form-control'}),
            'teacher_name': TextInput(attrs={'class': 'form-control'}),
            'teacher_qual': SelectMultiple(attrs={'class': 'form-control'}),
            'teacher_grades': SelectMultiple(attrs={'class': 'form-control'}),
            'teacher_dob': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'teacher_doh': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'teachcourse': TextInput(attrs={'class': 'form-control'}),
            'objects_L': SelectMultiple(attrs={'class': 'form-control'}),
            'triningtype': TextInput(attrs={'class': 'form-control'}),
            'teacher_gender': Select(attrs={'class': 'form-control'})
        }
        labels = {
            "teacher_name": _('name'),
            "teacher_qual":  _('tqual'),
            "teachcourse":  _('teacher courses'),
            "triningtype":  _('trining type'),
            "teacher_doh":  _('date of hire'),
            "teacher_gender":  _('gender'),
        }