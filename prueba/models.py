from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Prueba(models.Model):
	nombre = models.CharField(max_length=100,
								help_text='Ingrese nombre')
	edad = models.IntegerField(help_text='Ingrese edad')
	usa_linux = models.BooleanField()
	archivo = models.FileField()

	def __str__(self):
		return self.nombre