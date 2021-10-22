from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views

from rest_framework.urlpatterns import format_suffix_patterns
from polls import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('Pacientes/', views.PacientesList.as_view()),
]
