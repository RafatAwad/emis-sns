from django.db.models import Model, CharField,ForeignKey,ImageField,DateField,EmailField,IntegerField, CASCADE, SET_NULL, ManyToManyField,TextField, FileField, BooleanField,ManyToOneRel
from parent.models import Parent as P_p
from address.models import Location
from student.utils import RefTable, ref_table_verbose
from django.utils.translation import gettext as _
from account.models import User
@ref_table_verbose(_('gender '), _('genders'))
class Gender(RefTable): pass

@ref_table_verbose(_('level '), _('levels'))
class SchoolLevel(RefTable): pass

@ref_table_verbose(_('type of Disability'), _('types of disabilities '))
class SPNType(RefTable): pass

@ref_table_verbose(_('grade '), _('grades') )
class Grade(RefTable): pass

@ref_table_verbose(_('year '), _('years'))
class Year(RefTable): pass

@ref_table_verbose(_('shift '), _('shifts'))
class Shift(RefTable): pass

@ref_table_verbose(_('school Gender '), _('School genders'))
class SchoolGender(RefTable): pass

@ref_table_verbose(_('relation'), _('relations'))
class Relation(RefTable): pass
@ref_table_verbose(_('rural'), _('rurals'))
class UrOrRu(RefTable): pass
@ref_table_verbose(_('family status'), _('families status'))
class FamilyStatus(RefTable): pass

@ref_table_verbose(_('live with'), _('live with'))
class LiveWith(RefTable): pass
@ref_table_verbose(_('socity type'), _('socities types'))
class SocityType(RefTable): pass

# class LevelGrades(Model):
#     level = ForeignKey(SchoolLevel, on_delete=CASCADE)
#     grades = ManyToOneRel(Grade, to="id", field_name="id",on_delete=SET_NULL)

#     def __str__(self):
#         if not self.level.name:
#             return ""
#         return str(self.level.name)
#     class Meta:
#         verbose_name        = _('level grades')
#         verbose_name_plural = _('levels grades')

# class GradeObjects(Model):
#     grade = ForeignKey(Grade, on_delete=CASCADE)
#     objects = ManyToManyField('teachers.ObjectsL', related_name="grades_objects")

#     def __str__(self):
#         if not self.grade.name:
#             return ""
#         return str(self.grade.name)
#     class Meta:
#         verbose_name        = _('grade objects')
#         verbose_name_plural = _('grades objects')


class School(Model):
    school_code = CharField(verbose_name= _('school code'), max_length=50)
    school_name = CharField(verbose_name= _('school name'),max_length=100, null=True, blank=True)
    school_address = ForeignKey(Location,  null=True, blank=True,on_delete=SET_NULL)
    school_phone_no = CharField(verbose_name=_('phone number'), max_length=100, null=True, blank=True)
    school_gender = ForeignKey(SchoolGender, on_delete=SET_NULL, blank=True, null=True)
    school_shift = ForeignKey(Shift, on_delete=SET_NULL, blank=True, null=True)
    school_levels = ManyToManyField(SchoolLevel, blank=True, related_name='schools_levels')
    
    def __str__(self):
        if not self.school_name:
            return ""
        return str(self.school_name)
    class Meta:
        verbose_name        = _('school')
        verbose_name_plural = _('schools')

class Document(Model):
    birth_cert = FileField(verbose_name=_('birth certificate'),upload_to='documents/', blank=True)
    last_cert = FileField(verbose_name=_('last result'),upload_to='documents/', blank=True)
    other_cert = FileField(verbose_name=_('other certificate'),upload_to='documents/', blank=True)

    class Meta:
        verbose_name        = _('document')
        verbose_name_plural = _('documents')

class StudentInfo(Model):
    emis_id = CharField(_('Emis id'), max_length=255, blank=True, null=False)
    name = CharField(_('name'),max_length=255,blank=False)
    photo = ImageField(_('student photo'),upload_to='student-photos/', blank=True, null=True)
    date_of_birth = DateField(_('date of birth'), null=False, blank=False)
    place_of_birth = CharField(verbose_name=_('Place of birth') ,max_length=100,blank=True, null=True)
    gender = ForeignKey(Gender,  null=True,blank=False, on_delete=SET_NULL)
    year =  ForeignKey(Year,  blank=True,  null=True, on_delete=SET_NULL)
    shift = ForeignKey(Shift,  null=True, blank=False, on_delete=SET_NULL)
    spn_type = ForeignKey(SPNType,  null=True, blank=False, on_delete=SET_NULL)
    father_job = CharField(verbose_name=_('father jop'), max_length=200, null=True, blank=True)
    mother_name = CharField(verbose_name=_('mother name'), max_length=255, null=True, blank=True)
    mother_work = CharField(verbose_name=_('mother work'), max_length=200, null=True, blank=True)
    family_status = ForeignKey(FamilyStatus, blank=False,  null=True, on_delete=SET_NULL)
    live_with = ForeignKey(LiveWith,  blank=False,  null=True, on_delete=SET_NULL)
    parent = ForeignKey(P_p, null=True, blank=True, on_delete=SET_NULL)
    relation = ForeignKey(Relation, null=True, blank=False, on_delete=SET_NULL)
    disease = CharField(verbose_name=_('diseases'), max_length=255, null=True, blank=True)
    address = ForeignKey(Location, null=True, blank=True, on_delete=SET_NULL)
    ur_or_ru = ForeignKey(UrOrRu,  blank=False,  null=True, on_delete=SET_NULL)
    socit = ForeignKey(SocityType,  blank=False,  null=True, on_delete=SET_NULL)
    documents = ForeignKey( Document,  null=True, blank=True, on_delete=SET_NULL)
    school = ForeignKey(School,  null=True,blank=False,  on_delete=SET_NULL)
    grade = ForeignKey(Grade, null=True,blank=False, on_delete=SET_NULL)
    edu_status = BooleanField(default=False, blank=True)
    skills = TextField(_("skills"), blank=True)
    checked = BooleanField(verbose_name=_('checking'), default=False)
    checked_by = ForeignKey('account.User',null=True, blank=True, on_delete=SET_NULL, related_name='checked_by')
    checked_date = DateField(verbose_name=_('checking date '), null=True)
    added_date = DateField(verbose_name=_('Add date '), auto_now_add=True)
    added_by = ForeignKey('account.User',null=True, blank=True, on_delete=SET_NULL, related_name='added_by')
    note = CharField(verbose_name=_('Note'), max_length=200, null=True, blank=True)


    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)
 
    class Meta:
        verbose_name        = _('Student')
        verbose_name_plural = _('Students')

