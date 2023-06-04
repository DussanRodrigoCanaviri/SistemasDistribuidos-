from django.db import models

# Create your models here.

class Persona(models.Model):
	nombres = models.CharField(max_length=20)
	apellidos = models.CharField(max_length=30)
	ci = models.CharField(max_length=10, unique=True)
	direccion = models.CharField(max_length=50)
	telefono = models.IntegerField()
	correo = models.EmailField(max_length=100)
	fecha_nacimiento = models.DateTimeField(null=True)

	def __str__(self):
		return f"{self.apellidos} {self.nombres}"

	class Meta:
		ordering = ["-apellidos", "nombres"]


class Cajera(models.Model):
	item = models.CharField(max_length=5, unique=True, help_text='Numero item')
	fecha_ingreso = models.DateField("Fecha ingreso: ")
	persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True) # persona_id

	def __str__(self):
		return self.item

class Socio(models.Model):
	numero = models.CharField(max_length=15, unique=True)
	fecha_ingreso = models.DateField("Fecha ingreso: ")
	persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True) # persona_id	

	def __str__(self):
		return self.numero

class Oficial(models.Model):
	item = models.CharField(max_length=5, unique=True, help_text='Numero item')
	fecha_ingreso = models.DateField("Fecha ingreso: ")
	persona = models.OneToOneField(Persona, on_delete=models.CASCADE, primary_key=True) # persona_id

	def __str__(self):
		return self.item