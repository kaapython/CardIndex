# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-08 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20190408_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query_client',
            field=models.ForeignKey(help_text='Личное дело', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.CardIndex'),
        ),
        migrations.AlterField(
            model_name='query',
            name='query_date',
            field=models.DateField(default=None, help_text='Дата запроса (01.01.2019)', null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='query_spec',
            field=models.ForeignKey(help_text='Специалист', null=True, on_delete=django.db.models.deletion.CASCADE, to='users.UsersProfile'),
        ),
    ]
