# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_auto_20150722_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajos',
            name='hora_final',
        ),
        migrations.RemoveField(
            model_name='trabajos',
            name='hora_inicio',
        ),
        migrations.AddField(
            model_name='trabajos',
            name='beneficio',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trabajos',
            name='horas_facturables',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
