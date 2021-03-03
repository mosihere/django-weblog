from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View


class RegisterUser(View):
    form_class = RegisterForm
    template = 'accounts/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            login(request, user)
            messages.success(request, "You're register in successfully", 'success')
            return redirect('blog:index')
        return render(request, self.template, {'form':form})



class UserLogin(View):
    form_class = LoginForm
    template = 'accounts/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "You're logged in successfully", 'success')
                return redirect('blog:index')
            messages.error(request, "Wrong username or password", 'danger')
        return render(request, self.template, {'form':form})


class UserLogout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "logged out successfully", "success")
        return redirect('blog:index')

