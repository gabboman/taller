# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coche',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=200)),
                ('matricula', models.CharField(max_length=25)),
                ('fecha_entrada', models.DateTimeField(verbose_name='fecha_entrada')),
                ('fecha_salida', models.DateTimeField(verbose_name='fecha_salida')),
                ('averia_reparada', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Pieza',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_pieza', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('fecha_entrada', models.DateTimeField(verbose_name='fecha_entrada_pieza')),
                ('coche', models.ForeignKey(to='gestion.Coche')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('sueldo_hora', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fecha_trabajo', models.DateTimeField(verbose_name='fecha_trabajo')),
                ('descripcion', models.CharField(max_length=1000)),
                ('horas_reales', models.FloatField()),
                ('horas_cobrables', models.FloatField()),
                ('coche', models.ForeignKey(to='gestion.Coche')),
                ('trabajador', models.ForeignKey(to='gestion.Trabajador')),
            ],
        ),
    ]
