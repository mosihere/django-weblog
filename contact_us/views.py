from django import http
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['message']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, ['elwindmorris@gmail.com', 'mosihere@gmail.com'])
                
            except BadHeaderError:
                return HttpResponse('Invalid Header Found!')

            return redirect('contact_us:success')

    return render(request, 'contact_us/contact_us.html', {"form":form})



def successView(request):
    return HttpResponse('Success! Thanks for your message.')