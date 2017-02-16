# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-21 08:00
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('nbsap', '0015_auto_20161020_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='RamsarGoal',
            fields=[
                ('code', models.CharField(max_length=1,
                                          primary_key=True,
                                          serialize=False)),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='RamsarTarget',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=16)),
                ('aichi_targets', models.ManyToManyField(blank=True,
                 related_name='ramsar_targets',
                 db_constraint=False,
                 to='nbsap.AichiTarget')),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.AddField(
            model_name='ramsargoal',
            name='targets',
            field=models.ManyToManyField(
                related_name='ramsar_goals', to='nbsap.RamsarTarget'),
        )
    ]

    for i, lang in enumerate(settings.LANGUAGES):
        if i == 0:
            kw = {'blank': False, 'null': False}
        else:
            kw = {'blank': True, 'null': True}

        operations.append(
            migrations.AddField(
                model_name='ramsargoal',
                name='title_%s' % lang[0],
                field=models.TextField(
                    max_length=512, verbose_name=b'Title', **kw),
            )
        )
        operations.append(
            migrations.AddField(
                model_name='ramsargoal',
                name='description_%s' % lang[0],
                field=tinymce.models.HTMLField(
                    verbose_name=b'Description', **kw),
            )
        )
        operations.append(
            migrations.AddField(
                model_name='ramsartarget',
                name='description_%s' % lang[0],
                field=models.TextField(verbose_name=b'Description', **kw),
            )
        )