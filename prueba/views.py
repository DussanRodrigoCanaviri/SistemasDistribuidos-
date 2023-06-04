from django.http import HttpResponse
from datetime import datetime

def saludar(request):
	return HttpResponse("bienvenidos a la primera vista de Django")

def index(request):
	return HttpResponse("Pagina principal " )

def datos(request):
	return HttpResponse("hola " + nombres+ " tienes " + str(edad) + " años ")
