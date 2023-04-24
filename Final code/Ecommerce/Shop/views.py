from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from Shop.models import Sales, Service
from Shop.forms import SaleForm, ServiceForm
from django.contrib import messages

# Create your views here.

def home(request):
    sale=Sales.objects.all()
    return render(request , 'Shop/Home.html',{"object":sale})

def single(request):
    single=Sales.objects.get()
    return render(request, 'Shop/single.html',{"pro":single})

def sell(request): 
    if request.method == "POST":
        form = SaleForm(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'Shop/Home.html')


    return render(request , 'Shop/sell.html' )

def service(request):
    if request.method == "POST":
        serve = ServiceForm(request.POST or None)
        if serve.is_valid():
            serve.save()
        messages.success(request,('Your service request is submitted!'))
        return render(request, 'Shop/mech.html')
    
    return render(request, 'Shop/mech.html')


