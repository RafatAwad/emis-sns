from django.urls import path
from .views import teacher_delete,teacher_edit,teacher_list,teacher_list2,add_teacher,teacher_profile

urlpatterns = [
        path('teacher-list', teacher_list, name='teacher-list'),
        path('teacher-list2', teacher_list2, name='teacher-list2'),
        path('add-teacher/<school_code>', add_teacher, name='add-teacher'),
        path('edit/<int:id>', teacher_edit, name='teacher-edit'),
        path('delete/<int:id>', teacher_delete, name='teacher-delete'),
        path('teacher-profile/<int:id>', teacher_profile, name='teacher-profile'),
]
