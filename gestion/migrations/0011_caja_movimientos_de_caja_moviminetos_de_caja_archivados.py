# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0010_remove_trabajos_beneficios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('saldo_base', models.FloatField()),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Caja',
                'verbose_name_plural': 'Caja',
            },
        ),
        migrations.CreateModel(
            name='Movimientos_de_caja',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('fecha', models.DateTimeField(verbose_name='Fecha del movimiento')),
                ('descripcion', models.CharField(verbose_name='Descripción del moviento', max_length=200)),
                ('importe', models.FloatField()),
                ('caja', models.ForeignKey(to='gestion.Caja')),
                ('coche', models.ForeignKey(to='gestion.Coches')),
            ],
            options={
                'verbose_name': 'Movimientos de Caja',
                'verbose_name_plural': 'Movimientos de caja',
            },
        ),
        migrations.CreateModel(
            name='Moviminetos_de_caja_archivados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('fecha', models.DateTimeField(verbose_name='Fecha del movimiento')),
                ('movimientos', models.ForeignKey(to='gestion.Movimientos_de_caja')),
            ],
            options={
                'verbose_name': 'Movimientos de caja archivados',
                'verbose_name_plural': 'Movimientos de caja archivados',
            },
        ),
    ]
