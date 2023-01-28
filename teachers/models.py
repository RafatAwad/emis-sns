from django.db.models import Model, CharField,ForeignKey,DateField,CASCADE, SET_NULL, ManyToManyField, FileField, BooleanField
from address.models import Location
from student.models import School,Grade
from .utils import ref_table_verbose,RefTable
from django.utils.translation import gettext as _
from account.models import User

@ref_table_verbose(_('qualification '), _('qualifications') )
class TeachQual(RefTable): pass

@ref_table_verbose(_('object'), _('objects') )
class ObjectsL(RefTable): pass

class Teachers(Model):
    job_code =  CharField(verbose_name=_('job id'), max_length=100, null=False,blank=False)
    teacher_name = CharField(max_length=255, null=False,blank=False)
    teacher_qual = ManyToManyField(TeachQual)
    teacher_dob = DateField(verbose_name=_('date of birth') ,null=False,blank=False)
    teacher_doh = DateField(verbose_name=_('date of hire') ,null=True,blank=True)
    teacher_school = ForeignKey(School, null=True,on_delete=SET_NULL)
    teacher_grades = ManyToManyField(Grade)
    objects_L = ManyToManyField(ObjectsL)
    triningtype=CharField(verbose_name=_('training type'), max_length=100,null=True, blank=True)
    teacher_address = ForeignKey(Location, verbose_name=_('place of live'),null=True, on_delete=SET_NULL)
    teacher_gender = ForeignKey('student.Gender', max_length=50, null=True,blank=False, on_delete=SET_NULL)
    added_by = ForeignKey(User,null=True, blank=True, on_delete=SET_NULL)
    added_date = DateField(verbose_name=_('Add date '), auto_now_add=True)


    def __str__(self):
        if not self.teacher_name:
            return ""
        return str(self.teacher_name)
    class Meta:
        verbose_name        = _('teacher')
        verbose_name_plural = _('teachers')