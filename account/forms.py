from django.forms import NumberInput, ClearableFileInput, TextInput, Form, CharField, PasswordInput,EmailInput,Select
from .models import User
from django.utils.translation import gettext as _
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from captcha.fields import CaptchaField


class UserEditForm(UserChangeForm):  
    class Meta:  
        model = User  
        exclude = [
            'password','location'
        ]
        fields = ('username', 'email', 'first_name', 'last_name', 'photo', 'phone_number')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder':_('username')}),
            'email': EmailInput(attrs={'class': 'form-control','placeholder':_('email')}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'photo': ClearableFileInput(attrs={'class': 'form-control', 'accept': '.png, .jpg, .jpeg'}),
            'phone_number': TextInput(attrs={'class': 'form-control'}),
        }

class SignupForm(UserCreationForm):  
    class Meta:  
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'role')  
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder':_('username')}),
            'email': EmailInput(attrs={'class': 'form-control','placeholder':_('email')}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
            'role': Select(attrs={'class': 'form-control'}),
        }
class Signup2Form(UserCreationForm):  
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder':_('username')}),
            'email': EmailInput(attrs={'class': 'form-control','placeholder':_('email')}),
            'password1': PasswordInput(attrs={'class': 'form-control'}),
            'password2': PasswordInput(attrs={'class': 'form-control'}),
        }

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

#class UserInfoForm(ModelForm):

class AdminLoginForm(Form):
    captcha = CaptchaField()

    username = CharField(
        widget= TextInput(
            attrs={
                "placeholder": _("username"),
                "class": "form-control"
            }
        ))
    password = CharField(
        widget=PasswordInput(
            attrs={
                "placeholder": _("Password"),
                "class": "form-control"
            }
        ))


  