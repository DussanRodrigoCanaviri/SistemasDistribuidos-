from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	#return HttpResponse("Index de la aplicacion Ejemplo")
	return render(request,'index.html')

def saludo(request,nombres):
	#return HttpResponse("hola, saludos a: %s" %nombres)
	diccionario = {'nombres': nombres, 'edad': 19}
	return render(request,'saludar.html',diccionario)