# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_auto_20150720_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coches',
            options={'verbose_name': 'Coche', 'verbose_name_plural': 'Coches'},
        ),
        migrations.AlterModelOptions(
            name='piezas',
            options={'verbose_name': 'Piezas', 'verbose_name_plural': 'Piezas'},
        ),
        migrations.AlterModelOptions(
            name='proveedores',
            options={'verbose_name': 'Proveedores', 'verbose_name_plural': 'Proveedores'},
        ),
        migrations.AlterModelOptions(
            name='trabajadores',
            options={'verbose_name': 'Trabajadores', 'verbose_name_plural': 'Trabajadores'},
        ),
        migrations.AlterModelOptions(
            name='trabajos',
            options={'verbose_name': 'Trabajos', 'verbose_name_plural': 'Trabajos'},
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='telefono',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")], blank=True, max_length=15),
        ),
    ]
