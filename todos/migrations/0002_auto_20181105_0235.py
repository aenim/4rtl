# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-04 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='company name')),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='company',
            field=models.ManyToManyField(to='todos.Company'),
        ),
    ]