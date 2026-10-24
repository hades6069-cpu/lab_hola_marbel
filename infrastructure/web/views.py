from django.shortcuts import render

from application.services.saludar_service import SaludarService
from domain.persona import Persona


def home(request):
    saludo = SaludarService().ejecutar(Persona(nombre='Marbel'))
    return render(request, 'home.html', {'saludo': saludo})