# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20150716_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='proveedores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cif', models.CharField(max_length=9)),
                ('nombreempresa', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.PositiveIntegerField(max_length=9)),
            ],
        ),
    ]
