# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-05 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20190405_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_date',
            field=models.DateTimeField(blank=True, default=None, help_text='Время запроса', null=True),
        ),
    ]