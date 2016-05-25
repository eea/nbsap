# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('nbsap', '0004_auto_20160511_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='nationalaction',
            name='parent',
            field=models.ForeignKey(
                blank=True, null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='children',
                to='nbsap.NationalAction'),
        ),
    ]
