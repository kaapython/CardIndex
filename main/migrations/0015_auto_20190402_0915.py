# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-02 01:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20190402_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardindex',
            name='spec',
            field=models.ForeignKey(blank=True, default='в архиве', on_delete=django.db.models.deletion.CASCADE, to='users.UsersProfile', verbose_name='Движение ЛД по специалистам'),
        ),
    ]