from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ParentForm, ParentAddressForm
from .models import Parent, Location
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required
def parents_list(request):
    if request.user.role.id == 3 and request.user.location.district :
        parents = Parent.objects.filter(added_by = request.user).order_by('-added_date')
    elif request.user.role.id == 2 and request.user.location.governorate:
        parents = Parent.objects.filter(added_by = request.user).order_by('-added_date')
    else :
        parents = Parent.objects.order_by('-added_date')
        
    paginator = Paginator(parents, 20) 
    page_number = request.GET.get('page')
    parents_with_pag = paginator.get_page(page_number)
    context = {'items': parents_with_pag, 'url':'parents-list2'}
    return render(request, 'parents/parents-list.html', context)

@login_required
def parents_list2(request):
    if request.user.role.id == 3 and request.user.location.district :
        parents = Parent.objects.filter(added_by = request.user).order_by('-added_date')
    elif request.user.role.id == 2 and request.user.location.governorate:
        parents = Parent.objects.filter(added_by = request.user).order_by('-added_date')
    else :
        parents = Parent.objects.order_by('-added_date')
        
    paginator = Paginator(parents, 20) 
    page_number = request.GET.get('page')
    parents_with_pag = paginator.get_page(page_number)
    context = {'items': parents_with_pag, 'url':'parents-list2'}
    return render(request, 'partial/parents.html', context)

@login_required
def parent_profile(request, id):
    parent = Parent.objects.get(id=id)
    context = {
        'parent': parent
    }
    return render(request, 'parents/parent-profile.html', context)

@login_required
def parent_edit(request, id):
    parent = Parent.objects.get(id=id)
    parent_form = ParentForm(instance=parent)
    parent_address_form = ParentAddressForm(instance=parent.parent_address)
    if request.method == 'POST':
        parent_form = ParentForm(request.POST, request.FILES, instance=parent)
        if  parent_form.is_valid():
            parent_info = parent_form.save(commit=False)
            if request.POST['district']:
                s1 = Location.objects.get(id = request.POST.get('district'))
                parent_info.parent_address = s1
            elif request.POST['governorate']:
                s1 = Location.objects.get(id = request.POST.get('governorate'))
                parent_info.parent_address = s1
                
            parent_info.save()
            return redirect('parents-list')

    context = {
        'parent_form': parent_form,
        'parent_address_form': parent_address_form,
    }
    return render(request, 'parents/parent-edit.html', context)
@login_required
def parent_delete(request, id):
    parent = Parent.objects.get(id=id)
    parent.delete()
    return redirect('parents-list')

@login_required
def add_parent(request):
    parent_form = ParentForm(request.POST or None, request.FILES or None)
    parent_address_form = ParentAddressForm(request.POST or None)
    if request.method == 'POST':
        if parent_form.is_valid() and parent_address_form.is_valid():
            parent_info = parent_form.save(commit=False)
            if request.POST['district']:
                s1 = Location.objects.get(id = request.POST.get('district'))
                parent_info.parent_address = s1
            elif request.POST['governorate']:
                s1 = Location.objects.get(id = request.POST.get('governorate'))
                parent_info.parent_address = s1
            parent_info.added_by = request.user
            parent_info.save()
            messages.success(request,"تم إضافة ولي الأمر بنجاح")
            return redirect('parents-list')
    context = {
        'parent_form': parent_form,
        'parent_address_form': parent_address_form,

    }
    return render(request, 'parents/parent-registration.html', context)

