from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def contact_form(request):
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['mosihere@gmail.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('blog:index', {'form':form})
    else:
        form = ContactForm()
        return render(request, 'contact_us/contact_us.html', {'form':form})