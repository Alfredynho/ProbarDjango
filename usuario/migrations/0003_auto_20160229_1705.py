# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 21:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20160229_1645'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estudiante',
            options={'ordering': ('nombre',), 'verbose_name': 'Registro estudiante'},
        ),
        migrations.AlterModelOptions(
            name='registro_materia',
            options={'verbose_name': 'REgistro Materia', 'verbose_name_plural': 'Registro Materias'},
        ),
    ]
