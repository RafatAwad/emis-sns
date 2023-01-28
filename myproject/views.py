from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from student.models import StudentInfo, School
from parent.models import Parent
from teachers.models import Teachers
from address.models import Governorate,District
from account.models import User

def statics(request):
    
  return render(request, 'home/statics.html', {})
  
def governorates(request):
    if request.user.role.id == 1:
        address = Governorate.objects.all().order_by('name')
    elif request.user.role.id == 2:
        address = District.objects.filter(governorate = request.user.location.id).order_by('id')

           
    return render(request, 'home/governorate.html', { 'addresses': address})


@login_required(login_url='login')
def home_page(request):
    context = {}
    address = None
    if request.user.role.id == 1:
        users = User.objects.all()
        gov_users = users.filter(role = 2).count()
        gov_users_active = users.filter(role = 2).exclude(is_active = False).count()
        dist_users = users.filter(role = 3).count()
        dist_users_active = users.filter(role = 3).exclude(is_active = False).count()

        raw = StudentInfo.objects.all()
        total_student = raw.count()
        total_checked = raw.exclude(checked = False).count()
        total_parent = Parent.objects.count()
        total_schools = School.objects.count()
        total_teachers = Teachers.objects.count()
        address = Governorate.objects.all().order_by('id')
        st_1 = raw.filter(spn_type = 1).count()
        if st_1:
            st_1_per = (st_1 / total_student * 100).__ceil__
        st_2 = raw.filter(spn_type = 2).count()
        if st_1:
            st_2_per = (st_2 / total_student * 100).__ceil__
        st_3 = raw.filter(spn_type = 3).count()
        st_3_per = (st_3 / total_student * 100).__ceil__
        st_4 = raw.filter(spn_type = 4).count()
        st_4_per = (st_4 / total_student * 100).__ceil__
        context.update( {'schools': total_schools,'dist_users':dist_users, "gov_users": gov_users, 'gov_users_active': gov_users_active,'dist_users_active': dist_users_active}
        )
    elif request.user.role.id == 2:
        user_student = StudentInfo.objects.filter(checked_by = request.user).count()
        users = User.objects.filter(user_added_by = request.user.id)
        user_users = users.count()
        user_users_active = users.exclude(is_active = False).count()

        raw = StudentInfo.objects.filter(address__governorate = request.user.location.governorate)
        total_student = raw.count()
        total_checked = raw.exclude(checked = False).count()
        st_1 = raw.filter(spn_type = 1).count()
        st_1_per = (st_1 / total_student * 100).__ceil__
        st_2 = raw.filter(spn_type = 2).count()
        st_2_per = (st_2 / total_student * 100).__ceil__
        st_3 = raw.filter(spn_type = 3).count()
        st_3_per = (st_3 / total_student * 100).__ceil__
        st_4 = raw.filter(spn_type = 4).count()
        st_4_per = (st_4 / total_student * 100).__ceil__
        total_parent = Parent.objects.filter(parent_address__governorate = request.user.location.governorate).count()
        total_teachers = Teachers.objects.filter(teacher_address__governorate = request.user.location.governorate).count()
        address = District.objects.filter(governorate = request.user.location.id).order_by('id')
        user_teachers= Teachers.objects.filter(added_by = request.user).count()
        #percent = (total_checked / total_student * 100).__ceil__
        percent_user = (user_student/total_student * 100).__ceil__
        context.update(
             {'user_students': user_student, 'data_entries': user_users, 'de_active': user_users_active,'teachers_t':user_teachers,'percent_user':percent_user
             }
        )
    elif request.user.role.id  == 3:
        #user entries stats
        raw = StudentInfo.objects.filter(added_by = request.user)
        user_student = raw.count()
        user_checked = raw.exclude(checked = False).count
        user_teachers= Teachers.objects.filter(added_by = request.user).count()


        #all district entries
        raw2 = StudentInfo.objects.filter(address__district = request.user.location.district)
        total_student = raw2.count()
        total_checked = raw2.exclude(checked = False).count()
        st_1 = raw2.filter(spn_type = 1).count()
        st_1_per = (st_1 / total_student * 100).__ceil__
        st_2 = raw2.filter(spn_type = 2).count()
        st_2_per = (st_2 / total_student * 100).__ceil__
        st_3 = raw2.filter(spn_type = 3).count()
        st_3_per = (st_3 / total_student * 100).__ceil__
        st_4 = raw2.filter(spn_type = 4).count()
        st_4_per = (st_4 / total_student * 100).__ceil__
        percent_user = (user_student/total_student * 100).__ceil__

        total_parent = Parent.objects.filter(parent_address__district = request.user.location.district).count()
        total_teachers = Teachers.objects.filter(teacher_address__district = request.user.location.district).count()
        context.update(
            {'user_students': user_student, 'user_checked': user_checked,'teachers_t':user_teachers,'percent_user':percent_user

             }
        )
    else:
        raw = StudentInfo.objects.all()
        total_student = raw.count()
        total_checked = raw.exclude(checked = False).count()
        total_parent = Parent.objects.count()
        total_schools = School.objects.count()
        total_teachers = Teachers.objects.count()
        
    context.update({
        'student': total_student,
        'students_checked': total_checked,
        'parent': total_parent,
        'teachers': total_teachers,
        'addresses': address,
        'st_1': st_1, 'st_1_per': st_1_per,
        'st_2': st_2, 'st_2_per': st_2_per,
        'st_3': st_3, 'st_3_per': st_3_per,
        'st_4': st_4, 'st_4_per': st_4_per,
    })
    return render(request, 'home.html', context)