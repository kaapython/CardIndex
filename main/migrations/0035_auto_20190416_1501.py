# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-16 07:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20190416_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardindex',
            name='spec',
            field=models.ForeignKey(default=0, help_text='Движение ЛД', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UsersProfile', verbose_name='Движение ЛД по специалистам'),
        ),
    ]
