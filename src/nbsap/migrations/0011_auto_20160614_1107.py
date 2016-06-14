# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-14 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('nbsap', '0010_auto_20160613_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='euaction',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nbsap.Region'),
        ),
    ]
