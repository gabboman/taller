# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_auto_20150722_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabajos',
            name='beneficios',
        ),
    ]
