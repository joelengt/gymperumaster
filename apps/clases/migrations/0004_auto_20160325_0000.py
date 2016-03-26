# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-25 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clases', '0003_auto_20160322_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aerobicos',
            name='tipo',
            field=models.CharField(choices=[('PRINCIPAL', 'PRINCIPAL'), ('X-BOX', 'X-BOX'), ('FULL DAY', 'FULL DAY'), ('E-FITH', 'E-FITH'), ('AERODANCE', 'AERODANCE'), ('BODY-FIT', 'BODY-FIT'), ('BAILE', 'BAILE'), ('LOCALIZADO', 'LOCALIZADO'), ('STEP LOCAL', 'STEP LOCAL')], max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='bestcyclng',
            name='tipo',
            field=models.CharField(choices=[('PRINCIPAL', 'PRINCIPAL'), ('SPINNING', 'SPINNING'), ('SPINNINGFU', 'SPINNING TRABAJO DE FUERZA'), ('SPINNINGI', 'SPINNING TRABAJO DE INTERVALO'), ('SPINNINGFO', 'SPINNING TRABAJO DE FONDO'), ('BESET CYCLING', 'BEST CYCLING')], max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='deportesdecontacto',
            name='tipo',
            field=models.CharField(choices=[('PRINCIPAL', 'PRINCIPAL'), ('KARATE', 'KARATE'), ('BOXEO', 'BOXEO'), ('MMA WORKOUT', 'MMA WORKOUT'), ('KING BOXING', 'KING BOXING'), ('MUAY THAI', 'MUAY THAI'), ('CAPOEIRA', 'CAPOEIRA')], max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='talleres',
            name='tipo',
            field=models.CharField(choices=[('PRINCIPAL', 'PRINCIPAL'), ('BAILE MODERNO', 'BAILE MODERNO'), ('FULL BODY KIDS', 'FULL BODY KIDS'), ('MARINERA', 'MARINERA')], max_length=30, unique=True),
        ),
    ]