# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myquiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_text', models.CharField(max_length=200)),
                ('point', models.IntegerField(default=0)),
            ],
        ),
    ]
