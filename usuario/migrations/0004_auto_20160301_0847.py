# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20160229_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='apellidos',
            field=models.CharField(blank=True, help_text='Ingrese apellido aqui', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(blank=True, help_text='Ingrese nombre aqui', max_length=100, null=True),
        ),
    ]
