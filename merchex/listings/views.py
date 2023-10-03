# listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing


# Create your views here.

def bandList(request):  # la fonction de vue de Band 
   bands = Band.objects.all()
   return render(request,'listings/bandList.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band}) 

def about(request):
    listing = Listing.objects.all()
    return render(request,'listings/about.html', {'listings': listings})

def listings(request):
    return render(request,'listings/listings.html')

def contact(request):
    return render(request,'listings/contact.html')


