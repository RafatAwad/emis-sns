from django.shortcuts import render
from .models import Location, Governorate,District,Village,SubDistrict,SubVillage
from .forms import *
from student.filters import SchoolFilter
from student.models import School
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator 

@login_required
def address_teacher(request): 
    governorate = request.GET.get('governorate')
    district = District. objects.filter(governorate=governorate).order_by("name")
    district_id = request.GET.get('district')
    sub_district = SubDistrict.objects.filter(district=district_id).order_by('name')
    sub_district_id = request.GET.get('sub_district')
    village = Village.objects.filter(sub_district=sub_district_id).order_by('name')
    village_id = request.GET.get('village')
    sub_village = SubVillage.objects.filter(village=village_id).order_by('name')
    context = {
        'district': district,
        'sub_district': sub_district,
        'village': village,
        'sub_village': sub_village,
    }
    return render(request, 'partial/address_teacher.html', context)
   
@login_required
def load_school_entry(request): 
    governorate = request.GET.get('governorate')
    district = District.objects.filter(governorate=governorate).order_by('name')
    district_id = request.GET.get('district')
    sub_district = SubDistrict.objects.filter(district=district_id).order_by('name')
    sub_district_id = request.GET.get('sub_district')
    village = Village.objects.filter(sub_district=sub_district_id).order_by('name')
    village_id = request.GET.get('village')
    sub_village = SubVillage.objects.filter(village=village_id).order_by('name')
    school_address = request.GET.get('sub_village')
    school = School.objects.filter(school_address=school_address).order_by('school_name')
    context = {
        'district': district,
        'sub_district': sub_district,
        'village': village,
        'sub_village': sub_village,
        'school': school,
    }
    return render(request, 'partial/dropdown_list_enrty.html', context) 

@login_required
def governorate_filter(request): 
    governorate = request.GET.get('governorate')
    district = District.objects.filter(governorate=governorate).order_by('-name')

    context = {
        'district': district,

    }
    return render(request, 'partial/dropdown_list_enrty.html', context) 
