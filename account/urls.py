from django.urls import path
from .views import profile, update_profile, admin_login, admin_logout, settings_page,password_change,password_reset_request,passwordResetConfirm,signup,activate,user_delete,users_list,district_users,signup2,enable_user,disable_user

urlpatterns = [
    path('login', admin_login, name='login'),
    path('logout', admin_logout, name='logout'),
    path('signup', signup, name='signup'),
    path('signup2', signup2, name='signup2'),
    path('users', users_list, name='users-list'),
    path('district-users', district_users, name='district-users'),
    path('user-delete/<int:id>', user_delete, name='user-delete'),
    path("password-change", password_change, name="password-change"),
    path("password-reset", password_reset_request, name="password-reset"),
    path('reset/<uidb64>/<token>', passwordResetConfirm, name='password-reset-confirm'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  activate, name='activate'),  
    path('profile/<int:id>', profile, name='profile'),
    path('update/<int:id>', update_profile, name='update-profile'),
    path('password/', password_change, name='password'),
    path('settings/', settings_page, name='settings-page'),
    path('enable-user/<int:id>', enable_user, name='enable-user'),
    path('disable-user/<int:id>', disable_user, name='disable-user'),
]