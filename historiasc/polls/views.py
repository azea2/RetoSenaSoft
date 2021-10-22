from django import http
from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from .models import Pacientes

def index(request):
    return HttpResponse("Index")

def vistaPacientes(request):
    
    x = Pacientes.objects.all()

    return HttpResponse(x)
