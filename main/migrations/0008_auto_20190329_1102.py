# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-29 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190325_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardindex',
            name='ipd',
            field=models.IntegerField(verbose_name='Индивидуальное порядковое дело'),
        ),
    ]
