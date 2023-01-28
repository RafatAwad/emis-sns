from django.contrib import admin
from .models import Governorate, District, SubDistrict, Village, SubVillage, Location, LocationType


admin.site.register(Governorate)
admin.site.register(District)
admin.site.register(SubDistrict)
admin.site.register(Village)
admin.site.register(SubVillage)
admin.site.register(Location)
admin.site.register(LocationType)