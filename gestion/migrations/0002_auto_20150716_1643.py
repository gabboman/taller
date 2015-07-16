# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piezas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_pieza', models.CharField(max_length=200)),
                ('precio', models.FloatField()),
                ('fecha_entrada', models.DateTimeField(verbose_name=b'fecha_entrada_pieza')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajadores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.CharField(max_length=9)),
                ('nombre', models.CharField(max_length=50)),
                ('sueldo_hora', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Trabajos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_trabajo', models.DateTimeField(verbose_name=b'fecha_trabajo')),
                ('descripcion', models.CharField(max_length=1000)),
                ('hora_inicio', models.TimeField()),
                ('hora_final', models.TimeField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Coche',
            new_name='Coches',
        ),
        migrations.RemoveField(
            model_name='pieza',
            name='coche',
        ),
        migrations.RemoveField(
            model_name='trabajo',
            name='coche',
        ),
        migrations.RemoveField(
            model_name='trabajo',
            name='trabajador',
        ),
        migrations.RenameField(
            model_name='coches',
            old_name='averia_reparada',
            new_name='descripcion_averia',
        ),
        migrations.DeleteModel(
            name='Pieza',
        ),
        migrations.DeleteModel(
            name='Trabajador',
        ),
        migrations.DeleteModel(
            name='Trabajo',
        ),
        migrations.AddField(
            model_name='trabajos',
            name='coche',
            field=models.ForeignKey(to='gestion.Coches'),
        ),
        migrations.AddField(
            model_name='trabajos',
            name='pieza',
            field=models.ForeignKey(to='gestion.Piezas'),
        ),
        migrations.AddField(
            model_name='trabajos',
            name='trabajador',
            field=models.ForeignKey(to='gestion.Trabajadores'),
        ),
        migrations.AddField(
            model_name='piezas',
            name='coche',
            field=models.ForeignKey(to='gestion.Coches'),
        ),
    ]
