# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-08 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20190408_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_date',
            field=models.DateField(blank=True, default=None, help_text='Дата запроса', null=True),
        ),
    ]
