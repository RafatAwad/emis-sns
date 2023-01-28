from django.urls import path
from .views import student_delete,student_edit,student_list,student_list2,student_profile,student_registration,sch_delete,sch_profile,schools_list,schools_list2,print_form,sch_edit,add_student,check_now,gov_schools,check_edit,recheck,export_stu

urlpatterns = [
        path('schools-list', schools_list, name='schools-list'),
        path('schools-list2', schools_list2, name='schools-list2'),
        path('sch-profile/<school_code>', sch_profile, name='school-profile'),
        path('sch-edit/<school_code>', sch_edit, name='school-edit'),
        path('school-delete/<school_code>', sch_delete, name='school-delete'),
        path('student-list', student_list, name='student-list'),
        path('student-list2', student_list2, name='student-list2'),
        path('student-registration', student_registration, name='student-registration'),
        path('add-student/<school_code>', add_student, name='add-student'),
        path('profile/<emis_id>', student_profile, name='student-profile'),
        path('edit/<emis_id>', student_edit, name='student-edit'),
        path('delete/<emis_id>', student_delete, name='student-delete'),
        path('printf/', print_form, name='printf'),
        path('check-now/<emis_id>', check_now, name='check-now'),
        path('recheck/<emis_id>', recheck, name='recheck'),
        path('check-edit/<emis_id>', check_edit, name='check-edit'),
        path('gove-schools/<id>', gov_schools, name='gov-schools'),
        path('export-stu/<gov>', export_stu, name='export-stu'),

]
