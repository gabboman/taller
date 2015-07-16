# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_proveedores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
