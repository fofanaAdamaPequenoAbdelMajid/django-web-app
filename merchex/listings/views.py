# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Notice


# Create your views here.

def hello(request):
    bands = Band.objects.all()
    return render(request,'listings/hello.html', {'bands': bands})

def about(request):
    notices = Notice.objects.all()
    return render(request,'listings/about.html', {'notices': notices})

def listings(request):
    return render(request,'listings/listings.html')

def contact(request):
    return render(request,'listings/contact.html')
