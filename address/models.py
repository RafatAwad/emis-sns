from enum import unique
from django.db.models import Model, CharField, ForeignKey, CASCADE, SET_NULL,TextField
from student.utils import RefTable, ref_table_verbose
from django.utils.translation import gettext as _

@ref_table_verbose(_('location type'), _('location types '))
class LocationType(RefTable): pass

class Governorate(Model):
    id = CharField(_('governorate code'), max_length=50, primary_key=True, null=False)
    name = CharField(_('governorate') , max_length=45, null=True, blank=True)
    notes = CharField(_('notes'), max_length=200, null=True, blank=True)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)


    class Meta:
        verbose_name        = _('governorate')
        verbose_name_plural = _('governorates')

class District(Model):
    id = CharField(_('district code'), max_length=50,primary_key=True, null=False)
    name = CharField(_('district'), max_length=100, null=True, blank=True)
    governorate = ForeignKey(Governorate, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)


    class Meta:
        verbose_name        = _('district')
        verbose_name_plural = _('districts')

class SubDistrict(Model):
    id = CharField(_('subdistrict code'), max_length=50,primary_key=True, null=False)
    name = CharField(_('subdistrict'), max_length=100, null=True, blank=True)
    governorate = ForeignKey(Governorate,  on_delete=CASCADE, null=True, blank=True)
    district = ForeignKey(District, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)


    class Meta:
        verbose_name        = _('subdistrict')
        verbose_name_plural = _('subdistricts')
class Village(Model):
    id = CharField(_('village code'), max_length=50, null=False, primary_key=True)
    name = CharField(_('village'),max_length=100, null=True, blank=True)
    governorate = ForeignKey(Governorate, on_delete=CASCADE, null=True, blank=True)
    district = ForeignKey(District, on_delete=CASCADE, null=True, blank=True)
    sub_district = ForeignKey(SubDistrict, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)


    class Meta:
        verbose_name        = _('village')
        verbose_name_plural = _('villages')
class SubVillage(Model):
    id = CharField(_('subvillage code'), max_length=50, null=False, primary_key=True)
    name = CharField(_('subvillage'),max_length=100,  null=True, blank=True)
    governorate = ForeignKey(Governorate, on_delete=CASCADE, null=True, blank=True)
    district = ForeignKey(District, on_delete=CASCADE, null=True, blank=True)
    sub_district = ForeignKey(SubDistrict, on_delete=CASCADE, null=True, blank=True)
    village = ForeignKey(Village, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)


    class Meta:
        verbose_name        = _('subvillage')
        verbose_name_plural = _('subvillages')
class Location(Model):
    id                  = CharField(_('ID'), primary_key=True, max_length=100)
    location_type       = ForeignKey(LocationType, null=True, blank=True, on_delete=SET_NULL)
    name                = CharField(_('Name'), max_length=255, null=True, blank=True)
    governorate         = ForeignKey(Governorate, on_delete=SET_NULL, null=True, blank=True)
    district            = ForeignKey(District, on_delete=SET_NULL, null=True, blank=True)
    sub_district        = ForeignKey(SubDistrict, on_delete=SET_NULL, null=True, blank=True)
    village             = ForeignKey ( Village,on_delete=SET_NULL,null=True, blank=True)
    sub_village         = ForeignKey(SubVillage, on_delete=SET_NULL, null=True, blank=True)
    notes               = TextField(_('notes'), null=True, blank=True)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)

    class Meta:
        verbose_name        = _('address')
        verbose_name_plural = _('addresses')