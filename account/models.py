from address.models import Location
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models import Model, ManyToManyField, CharField, EmailField,CASCADE,ImageField,ForeignKey,DateField,BooleanField,DateTimeField,SET_NULL,OneToOneField
from django.utils.translation import gettext as _
class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
       
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Role(Model):
    name = CharField(max_length = 50)
    is_active = BooleanField(default=False)
    created_date = DateTimeField(auto_now_add=True)
    modified_date = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name        = _('role')
        verbose_name_plural = _('roles')

class User(AbstractBaseUser, PermissionsMixin):
    username =  CharField(_("Username"), max_length=50, unique=True)
    email      = EmailField(_('Email'), unique=True, null=False) # mark the email address as unique and required
    first_name = CharField(_('First Name') ,max_length = 150, blank = True)
    last_name = CharField(_('Last Name'),max_length = 150, blank = True)
    photo     = ImageField(_('Profile Photo'), upload_to='admin/', blank=True)
    phone_number     = CharField(_('phone number'), max_length=11, blank=False, null=False)
    location    = ForeignKey(Location, verbose_name=_('work feild'), null=True, blank=True, on_delete=SET_NULL)
    user_added_by    = ForeignKey('self', null=True, blank=True, on_delete=SET_NULL)
    added_date  = DateField(_('Date Added'), null=True, blank=True, auto_now_add=True)
    role = ForeignKey(Role, on_delete=SET_NULL, null=True)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    date_joined = DateTimeField(auto_now_add=True)
    created_date = DateTimeField(auto_now_add=True)
    modified_date = DateTimeField(auto_now=True)
    last_login = DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'    # Tell Django mail is the USERNAME_FIELD
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return '{} {}'.format(self.get_full_name(), self.username)

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        verbose_name        = _('user')
        verbose_name_plural = _('users')
