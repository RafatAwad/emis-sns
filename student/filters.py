import django_filters
from django_filters import CharFilter,ModelChoiceFilter

from django.utils.translation import gettext as _
from .models import StudentInfo,School,Year,Grade
from address.models import Governorate,District

class StudentFilter(django_filters.FilterSet):
    address__governorate__name = ModelChoiceFilter( queryset=Governorate.objects.all(), label=_("governorate"))
    address__district__name = ModelChoiceFilter( queryset=District.objects.all(),label=_("district"))
    name = CharFilter(field_name="name", lookup_expr='contains', label=_("name"))   
    year = ModelChoiceFilter(queryset=Year.objects.all(), lookup_expr='exact', label=_("edu year"))   
    grade = ModelChoiceFilter(queryset=Grade.objects.all(), lookup_expr='exact', label=_("grade"))   
    class Meta:
        model = StudentInfo
        fields = ['year', 'name',  'grade']
        exclude = []
        labels = {
             "year": _('year'),
        }

class SchoolFilter(django_filters.FilterSet):
    school_name = CharFilter( lookup_expr='icontains', label="اسم المدرسة")
    school_address__governorate__name = ModelChoiceFilter( queryset=Governorate.objects.all(), label=_("governorate"))
    school_address__district__name = ModelChoiceFilter( queryset=District.objects.all(),label=_("district"))
    #school_levels = ModelMultipleChoiceFilter(queryset=SchoolLevel.objects.all(), lookup_expr='exact')
    class Meta:
        model = School
        fields = ['school_name']
        exclude = []
        widgets = {
        }

        
