# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index_page', '0003_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='consultation',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
