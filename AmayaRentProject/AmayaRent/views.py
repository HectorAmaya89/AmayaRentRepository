from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def inicio(request):
    
    return render(request, 'AmayaRent/inicio.html')


def quienes_somos(request):
    
    return render(request, 'AmayaRent/quienes_somos.html')


def propiedades(request):
    
    return render(request, 'AmayaRent/propiedades.html')

def contacto(request):
    
    return render(request, 'AmayaRent/contacto.html')