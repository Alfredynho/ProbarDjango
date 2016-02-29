# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class estudiante(models.Model):
	nombre = models.CharField(max_length=100,
								blank=True,
								null=True,
								help_text='Ingrese nombre ')
	apellidos = models.CharField(max_length=100,
								blank=True,
								null=True,
								help_text='Ingrese apellido')
	edad = models.IntegerField()

	def __str__(self):
		return self.nombre

	class Meta:
		ordering = ('nombre',) #para ordenar por nombre
		verbose_name = 'Registro estudiante' #cambia el titulo

class Registro_Materia(models.Model):
	fkmateria = models.ForeignKey(estudiante)
	materia = models.TextField('Materia',help_text = 'Descripción de la materia')
	fecha = models.DateField()

	def __str__(self):
		return u'%s |asignado| %s ' % (self.fkmateria, self.materia)

	class Meta:
		verbose_name=u'REgistro Materia'
		verbose_name_plural = 'Registro Materias'
