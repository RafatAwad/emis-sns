from .models import User
from .forms import  AdminLoginForm,SignupForm,UserEditForm,Signup2Form
from student.forms import StudentAddressForm2
from address.models import Location, District,Governorate
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from .decorators import user_not_authenticated,is_not_admin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import gettext as _
from .forms import SetPasswordForm,PasswordResetForm
from django.db.models.query_utils import Q
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from .token import account_activation_token
from django.utils.encoding import force_bytes,force_str
from .models import Role
from .filters  import UsersFilter
from django.core.paginator import Paginator

@login_required(login_url='login')
def disable_user(request, id):  
    get_user = User.objects.get(id = id)
    if request.user.role.id == 2 and get_user.role.id <= request.user.role.id:
        messages.error(request, 'لا يمكنك تعطيل مستخدم أعلى منك رتبة')
    else:
        if get_user.is_active == True:
            get_user.is_active = False
            get_user.save()
            messages.success(request, 'تم تعطيل المستخدم بنجاح')
        else :
            messages.error(request, 'لا يمكنك تعطيل مستخدم معطل من قبل ')
    if request.user.role.id == 2:  
        return redirect('district-users')
    else :
        return redirect('users-list')
    
@login_required(login_url='login')
def enable_user(request,id):  
    get_user = User.objects.get(id = id)
    if request.user.role.id == 2 and get_user.role.id <= request.user.role.id:
        messages.error(request, 'لا يمكنك تفعيل مستخدم أعلى منك رتبة')
    else:
        if get_user.is_active == False:
            get_user.is_active = True
            get_user.save()
            messages.success(request, 'تم تفعيل المستخدم بنجاح')
        else :
            messages.error(request, 'لا يمكنك تفعيل مستخدم مفعل من قبل ')
    if request.user.role.id == 2:  
        return redirect('district-users')
    else :
        return redirect('users-list')
    

@user_not_authenticated
def activate(request, uidb64, token):  
    user = User
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()
        messages.success(request, _('Thank you for your email confirmation. Now you can login your account.'))
        return redirect('login')  
    else:  
        messages.error(request, _('Activation link is invalid! please re confirmation proccess'))
        return redirect('login')  
    
@login_required(login_url='login')
@is_not_admin
def signup(request):  
    if request.method == 'POST':  
        form = SignupForm(request.POST)
        location = StudentAddressForm2(request.POST  or None)
        if form.is_valid() and location.is_valid(): 
            if request.POST['district']:
                location = Location.objects.get(id = request.POST['district'])
            elif request.POST['governorate']:
                location = Location.objects.get(id = request.POST['governorate'])
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False
            user.location = location
            user.save()
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = _('Activation link has been sent to your email id')
            message = render_to_string('account/acc_active_email.html', {  
                'user': user, 
                'location': user.location.name,
                'location_type': user.location.location_type,
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),
                "protocol": 'https' if request.is_secure() else 'http',

            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            messages.success(request, _('user have to confirm his email before login'))
            return redirect('users-list')
        messages.error(request, _('error oops'))

    else:  
        form = SignupForm()
        location = StudentAddressForm2()
    return render(request, 'account/signup.html', {'form': form, 'location':location})  


@login_required(login_url='login')
def signup2(request):
    form = Signup2Form(request.POST)
    districts = District.objects.filter(governorate = request.user.location.governorate)
    if request.method == 'POST':  
        form = Signup2Form(request.POST or None)
        if form.is_valid(): 
            if request.POST['district']:
                location = Location.objects.get(id = request.POST['district'])
            # save form in the memory not in database  
            user_id = User.objects.get(id = request.user.id)
            role = Role.objects.get(id = 3)
            user = form.save(commit=False)
            user.is_active = False
            user.location = location
            user.role = role
            user.user_added_by = user_id
            user.save()
            # to get the domain of the current site  
            current_site = get_current_site(request)  
            mail_subject = _('Activation link has been sent to your email id')
            message = render_to_string('account/acc_active_email.html', {  
                'user': user, 
                'location': user.location.name,
                'location_type': user.location.location_type,
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),
                "protocol": 'https' if request.is_secure() else 'http',
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                    mail_subject, message, to=[to_email]  
            )  
            email.send()  
            messages.success(request, _('user have to confirm his email before login'))
            return redirect('district-users')
        messages.error(request, _('error oops'))

    return render(request, 'account/signup2.html', {'form': form, 'districts': districts})  

@login_required(login_url='login')
@is_not_admin
def users_list(request):
    users = User.objects.order_by('-id')
    tableFilter = UsersFilter(request.GET, queryset=users)
    users = tableFilter.qs
    paginator = Paginator(users, 10) 
    page_number = request.GET.get('page')
    users_with_pag = paginator.get_page(page_number)
    context = {'items': users_with_pag,
               'tableFilter': tableFilter
               }
    return render(request, 'account/users-list.html', context)

@login_required(login_url='login')
def district_users(request):
    users = User.objects.filter(location__governorate = request.user.location.governorate).order_by('-added_date').exclude(role = request.user.role)
    tableFilter = UsersFilter(request.GET, queryset=users)
    user = tableFilter.qs
    paginator = Paginator(user, 10) 
    page_number = request.GET.get('page')
    users_with_pag = paginator.get_page(page_number)
    context = {'items': users_with_pag,
               'tableFilter': tableFilter
               }
    return render(request, 'account/district-users.html', context)

@login_required(login_url='login')
def user_delete(request,user_id):
    user_f = User.objects.get(id=user_id)
    user_f.delete()
    return redirect('users-list')

    
    
@user_not_authenticated
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = User.objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("account/template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request, _(" We ve emailed you instructions for setting your password, if an account exists with the email you entered You should receive them shortly.<br>If you dont receive an email, please make sure you've entered the address you registered with, and check your spam folder."))
                    return redirect('login')

                else:
                    messages.error(request, _("Problem sending reset password email, <b>SERVER PROBLEM</b>"))
            else:   
                messages.error(request, _("email not exsist"))
                return redirect('password-reset')
        
        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="account/password_reset.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    user = User
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, _("Your password has been set. You may go ahead and <b>log in </b> now."))
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'account/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, _("Link is expired"))

    messages.error(request, _('Something went wrong, redirecting back to Homepage'))
    return redirect("login")

@login_required(login_url='login')
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Your password has been changed"))
            return redirect('home')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'account/password_reset_confirm.html', {'form': form})

@login_required(login_url='login')
def profile(request, id):
    profile = User.objects.get(id=id)
    context = {
        'profile': profile
    }
    return render(request, 'account/profile.html', context)

@login_required(login_url='login')
def update_profile(request, id):
    context = {}
    profile = User.objects.get(id=id)
    #if user we want to update from district show districts in edit page
    if request.user.role.id == 2 and profile.role.id == 3:
        districts = District.objects.filter(governorate = profile.location.governorate)
        context.update({
            'districts': districts,
            'district_p': profile.location.district
        })
    elif request.user.role.id == 1:
        governorates = Governorate.objects.all()
        context.update({
            'governorates': governorates,
            'location': profile.location
        })
    forms = UserEditForm(instance=profile)
    if request.method == 'POST':
        forms = UserEditForm(request.POST or None, request.FILES or None, instance=profile)
        if forms.is_valid():
            if request.POST.get('district'):
                location = Location.objects.get(id = request.POST['district'])
            elif request.POST.get('governorate'):
                location = Location.objects.get(id = request.POST['governorate'])
            elif request.POST.get('district') and request.POST.get('governorate'):
                location = Location.objects.get(id = request.POST['district'])
            else:
                location = profile.location
            forms2 = forms.save(commit=False)
            forms2.location = location
            forms2.save()
            messages.success(request,_('user info updated successfully'))
            if request.user.role.id == 1:
                return redirect('users-list')
            elif request.user.role.id == 2:
                return redirect('district-users')
        messages.error(request,_('user info not updated !!'))
        if request.user.role.id == 1:
            return redirect('users-list')
        elif request.user.role.id == 2:
            return redirect('district-users')

    context.update({
        'forms': forms
    })
    return render(request, 'account/update-profile.html', context)

@user_not_authenticated
def admin_login(request):
    form = AdminLoginForm(request.POST or None)
    if request.method == 'POST':     
        if form.is_valid():
            human = True
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request,_("Login successfull"))
                return redirect('home')
        messages.error(request,_('Invalid credentials, Please check username/email or password. '))
    context = {'form': form}
    return render(request, 'account/login.html', context)

@login_required
def admin_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def settings_page(request):
    context ={}
    return render(request, 'settings.html', context)
