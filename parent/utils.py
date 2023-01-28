from django.db.models import Model, CharField
from django.utils.translation import gettext as _

def ref_table_verbose(verbose_name, verbose_name_plural = None):
    def wrapper(cls):
        if hasattr(cls, '_meta'):
            cls._meta.verbose_name = verbose_name
            if verbose_name_plural is None:
                cls._meta.verbose_name_plural = verbose_name
            else: cls._meta.verbose_name_plural = verbose_name_plural
        return cls
    return wrapper

class RefTable(Model):
    name = CharField(verbose_name=_('name'), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['pk']
        abstract = True