from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.models import MusicLibrary

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'Login Successful !!')
            return redirect('home')
        else:
            form = AuthenticationForm(request.POST)
            messages.info(request, 'Invalid Credentials !!')
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        
        return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
     
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
 
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            MusicLibrary.objects.create(user=user)
            messages.info(request, 'Registration Successful !!')
            return redirect('home')
         
        else:
            messages.info(request, 'Please Fix the given error !!')
            return render(request,'accounts/register.html',{'form':form})
     
    else:
        form = UserCreationForm()
        return render(request,'accounts/register.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Logout Successful !!')
    return redirect('home')