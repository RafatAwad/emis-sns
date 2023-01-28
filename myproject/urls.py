from django.contrib import admin
from django.urls import path, include
from .views import home_page,statics,governorates
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('account/', include('account.urls')),
    path('controller/', admin.site.urls, name='controller'),
    path('', home_page, name='home'),
    path('student/', include('student.urls')),
    path('parent/', include('parent.urls')),
    path('address/', include('address.urls')),
    path('teachers/', include('teachers.urls')),
    path('governorates/', governorates, name='governorates'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('statics/', statics, name="statics"),
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('captcha/', include('captcha.urls')),
]