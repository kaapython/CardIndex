# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-29 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190329_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='ipd',
        ),
        migrations.AddField(
            model_name='cardindex',
            name='ipd',
            field=models.IntegerField(default=1, verbose_name='Индивидуальное порядковое дело'),
            preserve_default=False,
        ),
    ]
