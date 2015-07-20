# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_auto_20150716_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piezas',
            name='fecha_entrada',
            field=models.DateTimeField(verbose_name='fecha_entrada_pieza'),
        ),
        migrations.AlterField(
            model_name='trabajos',
            name='fecha_trabajo',
            field=models.DateTimeField(verbose_name='fecha_trabajo'),
        ),
    ]
