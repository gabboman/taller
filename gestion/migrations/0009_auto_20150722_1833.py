# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0008_auto_20150722_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trabajos',
            old_name='beneficio',
            new_name='beneficios',
        ),
        migrations.AddField(
            model_name='trabajos',
            name='horas_reales',
            field=models.FloatField(default=0, verbose_name='Horas reales'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coches',
            name='fecha_entrada',
            field=models.DateTimeField(verbose_name='Fecha entrada'),
        ),
        migrations.AlterField(
            model_name='coches',
            name='fecha_salida',
            field=models.DateTimeField(verbose_name='Fecha salida'),
        ),
        migrations.AlterField(
            model_name='piezas',
            name='fecha_entrada',
            field=models.DateTimeField(verbose_name='Fecha de entrada la pieza'),
        ),
        migrations.AlterField(
            model_name='piezas',
            name='nombre_pieza',
            field=models.CharField(max_length=200, verbose_name='Nombre de la pieza'),
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='fecha_trabajo',
            field=models.DateTimeField(verbose_name='Fecha de intervención'),
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='horas_facturables',
            field=models.FloatField(verbose_name='Horas facturables'),
        ),
    ]
