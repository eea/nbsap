# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 12:19
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import tinymce.models


def load_fixtures(apps, schema_editor):
    call_command('load_fixtures')


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tct', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixtures)
    ]
