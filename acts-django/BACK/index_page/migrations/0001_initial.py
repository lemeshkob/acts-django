# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_field', models.TextField()),
                ('title', models.TextField(max_length=100)),
                ('published_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'News',
            },
        ),
    ]