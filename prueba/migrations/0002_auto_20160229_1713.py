# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prueba',
            name='nombre',
            field=models.CharField(help_text='Ingrese nombre', max_length=100),
        ),
    ]
