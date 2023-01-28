from django.db.models import Model, CharField,ForeignKey,ImageField,DateField,EmailField,IntegerField, CASCADE, SET_NULL, ManyToManyField, FileField, BooleanField
from address.models import Location
from account.models import User
from .utils import RefTable, ref_table_verbose
from django.utils.translation import gettext as _


@ref_table_verbose(_('ID Type '), _('ID Types') )
class IdType(RefTable): pass

class Parent(Model):
    parent_name = CharField(max_length=255,blank=False,null=False)
    parent_photo = ImageField(upload_to='parents-photos/',blank=True, null=True)
    parent_date_of_birth = DateField(verbose_name=_('date of birth') ,null=False,blank=False)
    parent_place_of_birth = CharField(verbose_name=_('Place of birth') ,max_length=200,blank=True, null=True)
    parent_gender = ForeignKey('student.Gender', blank=False, null=True, on_delete=SET_NULL)
    id_type = ForeignKey(IdType, null=True,blank=False, on_delete=SET_NULL)
    id_file = FileField(upload_to='documents/', blank=True, verbose_name=_('id file'))
    parent_phone_no = IntegerField(max_length=9, blank=False, null=False, verbose_name=_('phone number'))
    parent_address = ForeignKey(Location, verbose_name=_('place of live'), on_delete=SET_NULL, null=True, related_name='parents')
    added_by = ForeignKey(User,null=True, blank=True, on_delete=SET_NULL)
    added_date = DateField(verbose_name=_('Add date '), auto_now_add=True)


    def __str__(self):
        return self.parent_name
    class Meta:
        verbose_name        = _('parent')
        verbose_name_plural = _('parents')
