 
from django.shortcuts import render, redirect
from .forms import TeachersForm, TeacherstAddressForm,TeacherstAddressForm2
from .models import Teachers
from student.models import School
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from address.models import Location, District
from django.core.paginator import Paginator

@login_required
def teacher_profile(request, id):
    teacher = Teachers.objects.get(id=id)
    context = {
        'teacher': teacher
    }
    return render(request, 'teacher/teacher-profile.html', context)

@login_required
def teacher_edit(request,id):
    teacher = Teachers.objects.get(id=id)
    teacher_info = TeachersForm(instance=teacher)
    districts = District.objects.filter(governorate = teacher.teacher_address.governorate.id)
    address_form = TeacherstAddressForm(instance=teacher.teacher_address)
    address_form.district = districts
    if request.method == 'POST':
        teacher_form = TeachersForm(request.POST,instance=teacher)
        teacher_address_form =TeacherstAddressForm (request.POST,instance=teacher.teacher_address)
        if teacher_form.is_valid() and teacher_address_form.is_valid():
            s1 = teacher_address_form.save()
            teacher_info = teacher_form.save(commit=False)
            teacher_info.address = s1
            teacher_info.save()
            messages.success(request, "تمت عملية التعديل بنجاح" )
            return redirect('teacher-list')
        messages.error(request, "لم تتم عملية التعديل")
    context = {
        'teacher_info': teacher_info,
        'teacher_address_form': address_form,
    }
    return render(request, 'teacher/teacher-edit.html', context)

@login_required
def teacher_delete(request, id):
    teacher = Teachers.objects.get(id=id)
    teacher.delete()
    return redirect('teacher-list')

@login_required(login_url="login")
def add_teacher(request, school_code):
    school = School.objects.get(school_code = school_code)
    teacher_form = TeachersForm(request.POST  or None)
    if request.method == 'POST':
        if teacher_form.is_valid():
            if request.POST['school_code']:
                student_school = School.objects.get(school_code = request.POST['school_code'])
                teacher_address_form = Location.objects.get(id = request.POST['address'])

            teacher_info = teacher_form.save(commit=False)
            teacher_info.teacher_address = teacher_address_form
            teacher_info.teacher_school = student_school
            teacher_info.added_by = request.user
            teacher_info.save()
            messages.success(request,"تم إضافة المعلم بنجاح")
            return redirect('teacher-list')
    context = {
        'teacher_info': teacher_form,
        'school_info': school,
    }
    return render(request, 'teacher/teacher-registration.html', context)

@login_required
def teacher_list(request):
    context = {}
    if request.user.role.id == 3 and request.user.location.district :
            teachers = Teachers.objects.filter(added_by = request.user).order_by('-added_date')
    elif request.user.role.id == 2 and request.user.location.governorate:
        teachers = Teachers.objects.filter(teacher_school__school_address__governorate = request.user.location.governorate).order_by('-added_date')
    else :
        teachers = Teachers.objects.order_by('-added_date')
       

    paginator = Paginator(teachers, 20) 
    page_number = request.GET.get('page')
    teachers_with_pag = paginator.get_page(page_number)
    context.update({'items': teachers_with_pag,
                'url' : "teacher-list2"
               })
    return render(request, 'teacher/teacher-list.html', context)

@login_required
def teacher_list2(request):
    context = {}
    if request.user.role.id == 3 and request.user.location.district :
            teachers = Teachers.objects.filter(added_by = request.user).order_by('-added_date')
    elif request.user.role.id == 2 and request.user.location.governorate:
        teachers = Teachers.objects.filter(teacher_school__school_address__governorate = request.user.location.governorate).order_by('-added_date')
    else :
        teachers = Teachers.objects.order_by('-added_date')

    paginator = Paginator(teachers, 20) 
    page_number = request.GET.get('page')
    teachers_with_pag = paginator.get_page(page_number)
    context.update({'items': teachers_with_pag,
                'url' : "teacher-list2"
               })
    return render(request, 'partial/teachers.html', context)