from django.urls import path

from .views import parent_delete, parent_edit, parent_profile, parents_list,parents_list2,add_parent
urlpatterns = [
    path('parents-list', parents_list, name='parents-list'),
    path('parents-list2', parents_list2, name='parents-list2'),
    path('add-parent', add_parent, name='add-parent'),
    path('profile/<int:id>', parent_profile, name='parent-profile'),
    path('edit/<int:id>', parent_edit, name='parent-edit'),
    path('delete/<int:id>', parent_delete, name='parent-delete'),
]
