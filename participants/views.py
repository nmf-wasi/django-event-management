from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from participants.forms import SignUpForm,assignRoleForm, LoginForm, CreateGroupForm
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import login, logout, authenticate

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_organizer(user):
    return user.groups.filter(name='Organizer').exists()

def is_participant(user):
    return user.groups.filter(name='Participant').exists()


def sign_up(request):
    form=SignUpForm() 
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user._send_activation = True
            user.email=form.cleaned_data.get('email')
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active=False
            user.save()
            messages.success(request, "A Confirmation EMail has been sent to your email!\nCheck your email to activate your account")
            return redirect('sign_in')
        
        else:
            print("From isnt valid")
    
    context={"form":form}
    return render(request, "registration/sign_up.html", context)

def sign_in(request):
    form=LoginForm()
    if request.method=="POST":
        form=LoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
        
    context={'form':form}
    return render(request, "registration/sign_in.html", context)

@login_required
def sign_out(request):
    if request.method=='POST':
        logout(request)    
        return redirect('sign_in')
    return redirect('sign_in')

@user_passes_test(is_admin, login_url='noPermission')
def admin_Dashboard(request):
    users=User.objects.all()
    context={"users":users}
    return render(request, "admin/dashboard.html",context)

@user_passes_test(is_admin, login_url='noPermission')
def activate_user(request, user_id, token):
    try:
        user=User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active=True
            user.save()
            return redirect('sign_in')
        else: 
            return HttpResponse("Invalid ID or Token!")
    except User.DoesNotExist:
        return HttpResponse("User not found!")

@user_passes_test(is_admin, login_url='noPermission')
def assign_Role(request, user_id):
    user=User.objects.get(id=user_id)
    form=assignRoleForm()
    if request.method=="POST":
        form=assignRoleForm(request.POST)
        if form.is_valid():
            role=form.cleaned_data.get('role')
            user.groups.clear()
            user.groups.add(role)
            messages.success(request, f"User {user.username} has been assigned to the {role.name} role")
            return redirect('admin_Dashboard')
    context={"form":form}
    return render(request, 'admin/assign_role.html', context)

@user_passes_test(is_admin, login_url='noPermission')
def create_group(request):
    form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)

        if form.is_valid():
            group = form.save()
            messages.success(request, f"Group {group.name} has been created successfully")
            return redirect('admin_Dashboard')

    return render(request, 'admin/create_group.html', {'form': form})

def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()
    context = {"groups": groups}
    return render(request, 'admin/group_list.html', context)

@user_passes_test(is_admin, login_url='noPermission')
def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.method == 'POST':
        group.delete()
        messages.success(request, f"Group '{group.name}' has been deleted successfully.")
        return redirect('group_list')  # or wherever you want to redirect after deletion
    return 


@user_passes_test(is_admin, login_url='noPermission')
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, f"User '{user.first_name}' has been deleted successfully.")
        return redirect('admin_Dashboard')  # or wherever you want to redirect after deletion
    return 

def create_category(request):
    return render(request, "registration/sign_up.html")

def category_list(request):
    return render(request, "registration/sign_up.html")



@user_passes_test(is_admin, login_url='noPermission')
def create_participant(request):
    form=SignUpForm() 
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.email=form.cleaned_data.get('email')
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active=True
            user._send_activation = False
            user.save()
            messages.success(request, "Participant Created!")
            return redirect('sign_in')
        
        else:
            print("From isnt valid")
    
    context={"form":form}
    return render(request, "admin/create_participant.html", context)