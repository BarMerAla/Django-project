from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required




# Create your views here.

def user_register(request):
    if request.method == "POST":
        register_form = NewUserForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect('main:index')
            Profile.objects.create(user=user)    
    register_form = NewUserForm()
    return render(request=request, template_name='user_auth/register.html', context={'register_form': register_form})


def user_login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')
            
    login_form = AuthenticationForm()   
    return render(request=request, template_name='user_auth/login.html', context={'login_form': login_form})   

def user_logout(request):
    logout(request)
    return redirect('main:index')  


def user_cab(request):
    print(User.objects.all())
    username =  None
    if request.user.is_authenticated:
        username=request.user.username
        print(username)
    return render(request, 'user_auth/cab.html')


       
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                data=request.POST,
                                files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'user_auth/edit.html', {'user_form': user_form,
                                                'profile_form': profile_form})

            