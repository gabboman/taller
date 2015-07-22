# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0006_auto_20150721_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='coches',
            name='estado',
            field=models.CharField(max_length=1, default=0, choices=[('0', 'A la espera'), ('1', 'En proceso'), ('2', 'Finalizado'), ('3', 'Pagado')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='telefono',
            field=models.CharField(validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="El número debe de tener el siguiente formato: '+999999999'. Hasta un máximo de 15 dígitos.")], max_length=15, blank=True),
        ),
    ]
