from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from .models import Product, Order
import pywhatkit
from datetime import time
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def send(requset):
    if requset.method == "POST":
        email = requset.POST['email']
        message = requset.POST['message']
        sendmail = [email]
        send_mail(
            "Task Assign",
            message,
            'settings.EMAIL_HOST_USER',
            sendmail ,
            fail_silently = False
                )
        return render(requset, 'Purchase/task.html')
    
    return render(requset, 'Purchase/task.html')

