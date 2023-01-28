from django.urls import path
from.views import load_school_entry,address_teacher,governorate_filter


urlpatterns = [
         path('load-schools', load_school_entry, name='load-schools-entry'),
         path('load-district', governorate_filter, name='load-district'),
         path('address-teacher', address_teacher, name='address-teacher'),
]
