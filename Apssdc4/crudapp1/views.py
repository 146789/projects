from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.

def sendmail(request):
    return render(request, 'crudapp1/mail.html')
    
