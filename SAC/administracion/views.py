from django.shortcuts import render, HttpResponse, redirect
from models import Persona
# Create your views here.

def index(request):
	persona = Persona.objects.all()
	'''
	SELECT *
	FROM administracion_persona
	'''
	return render(request, 'persona/index.html',{'personas':personas})

def nuevo(request):
	if request.method== 'GET':
		return render(request, 'personas/nuevo.html')
	else:
		data =request.POST
		persona = Persona(
			nombres = data.get('nombres'),
			apellidos = data.get ('apellidos'),
			ci = data.get('ci'),
			direccion = data.get('direccion'),
			telefono = data.get('telefono'),
			fecha_nacimiento = data.get('fecha_nacimiento'),
			correo = data.get('correo')

			)
		persona.save()
		return redirect('persona_index')
	