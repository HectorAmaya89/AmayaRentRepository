from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    
    return render(request, 'AmayaRent/inicio.html')


def aboutus(request):
    
    return render(request, 'AmayaRent/aboutus.html')


def shop(request):
    
    return render(request, 'AmayaRent/shop.html')

def contactus(request):
    
    return render(request, 'AmayaRent/contactus.html')