import django_filters
from django_filters import CharFilter,ModelChoiceFilter

from django.utils.translation import gettext as _
from .models import User,Role
from address.models import Governorate,District


class UsersFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr='contains', label=_("name"))
    role = ModelChoiceFilter(queryset=Role.objects.all().order_by("id"), label=_("role"))
    location__governorate__name = ModelChoiceFilter( queryset=Governorate.objects.all().order_by("id"), label=_("governorate"))
 
    class Meta:
        model = User
        fields = ['name']

