from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username or Email'}))

    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))

    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))


    def clean_username(self):
        data = self.cleaned_data['username']
        user = User.objects.filter(username=data)
        if user.exists():
            raise ValidationError('This Username is already Exist')
        return data

    
    def clean_email(self):
        data = self.cleaned_data['email']
        user = User.objects.filter(email=data)
        if user.exists():
            ValidationError('This email is already in use ...')
        return data


    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get('password')
        p2 = cleaned_data.get('confirm_password')
        if p1 and p2:
            if p1 != p2:
                ValidationError('Your password not match !')
