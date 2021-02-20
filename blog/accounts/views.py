from django.forms import forms
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import loginForm, registerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You're logged in successfully", 'success')
                return redirect('blog:index')
            
            else:
                messages.warning(request, "Wrong username or password", 'danger')
    
    else:
        form = loginForm()
    
    return render(request, 'accounts/login.html', {'form':form})



def user_register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, "Your registeration complete", 'success')
            return redirect('accounts/user_login')
    else:
        form = registerForm()
    return render(request, 'accounts/register.html', {'form':form})



def user_logout(request):
    logout(request)
    messages.success(request, "logged out successfully", "success")
    return redirect('blog:index')
        