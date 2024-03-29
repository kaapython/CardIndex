# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-29 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('main', '0010_auto_20190329_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardindex',
            name='spec',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.UsersProfile', verbose_name='Движение ЛД'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cardindex',
            name='control',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.Control', verbose_name='Статус ЛД'),
        ),
    ]
