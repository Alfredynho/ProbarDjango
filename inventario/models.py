from __future__ import unicode_literals

from django.db import models

# Create your models here.
class estudiante(models.Model):
    diurno = 'di'
    tarde = 'tar'
    nocturno = 'noc'
    prueba = 'pr'
    estado_del_dia = (
        (diurno, 'DIURNO'),
        (tarde, 'TARDE'),
        (nocturno, 'NOCTURNO'),
        (prueba, 'PRUEBA'),
    )
    estado_dia = models.CharField(max_length=20,
                                      choices=estado_del_dia,
                                      default=diurno)

    def is_upperclass(self):
        return self.estado_dia in (self.nocturno, self.prueba)