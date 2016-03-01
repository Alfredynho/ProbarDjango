from __future__ import unicode_literals

from django.db import models

# Create your models here.
class estudiante(models.Model):
    diurno = 'di'
    tarde = 'tar'
    nocturno = 'noc'
    prueba = 'pr'
    MEDIA_CHOICES = (
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
    )
    estado_dia = models.CharField(max_length=20,
                                      choices=MEDIA_CHOICES,
                                      default=diurno)

    def is_upperclass(self):
        return self.estado_dia in (self.nocturno, self.prueba)