from django.contrib import admin
from django.db import models

from .models import Pacientes, Profesionales, Historialesclinicos

# Register your models here.


class PacientesAdmin(admin.ModelAdmin):
    list_display = (
        "idpacientes",
        "identificacion",
        "nombrecompleto")



class ProfesionalesAdmin(admin.ModelAdmin):
    list_display = (
        "idprofesional",
        "identificacion",
        "nombrecompleto",
        "especialidad",
        "firma",
        "usuario",
        "contrasenia")




class HistorialesclinicosAdmin(admin.ModelAdmin):
    list_display = (
        "idhistorialesclinicos",
        "fecha",
        "formato",
        "profesionales_idprofesional",
        "pacientes_idpacientes")


admin.site.register(Pacientes, PacientesAdmin)
admin.site.register(Profesionales, ProfesionalesAdmin)
admin.site.register(Historialesclinicos, HistorialesclinicosAdmin)
