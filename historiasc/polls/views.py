from django import http
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from polls.models import Pacientes, Profesionales, Historialesclinicos
from polls.serializers import PacientesSerializer

# Create your views here.

def index(request):
    return HttpResponse("Index")

class PacientesList(APIView):

    def get(self, request):
        Pacientes1 = Pacientes.objects.all()
        serializer = PacientesSerializer(Pacientes1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

