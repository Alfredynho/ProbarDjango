# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class usuarios(models.Model):
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
		ordering = ('nombre',)


class TodoArticulo(models.Model):
	fktodo = models.ForeignKey(usuarios)
	tarea = models.TextField('Tareas',help_text = 'Descripción de la tarea')
	fecha = models.DateField()

	def __str__(self):
		return u'%s |asignado| %s ' % (self.fktodo, self.tarea)

	class Meta:
		verbose_name=u'Todo Tarea'
		verbose_name_plural = 'Todo Tareas'
