from __future__ import unicode_literals

from django.db import models
#Creando los modelos para la base de datos del registro de docentes
# Create your models here.
class Registro_docente(models.Model):
	nombre = models.CharField(max_length=200,blank=True, null=True)
	email = models.EmailField()
	codigo_postal=models.IntegerField()
	registro =models.DateTimeField(auto_now_add=True , auto_now = False)
	actualizado = models.DateTimeField(auto_now_add= False , auto_now = True)

	def __str__(self):
		return self.nombre