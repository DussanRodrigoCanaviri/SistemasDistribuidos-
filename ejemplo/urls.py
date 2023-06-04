from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='ejemplo_index'),
	path('saludo/<str:nombres>',views.saludo,name='ejemplo_saludar')
]