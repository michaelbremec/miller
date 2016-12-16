# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 14:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0054_auto_20161214_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='interdiciplinarity',
            new_name='interdisciplinarity',
        ),
        migrations.RemoveField(
            model_name='review',
            name='interdiciplinarity_score',
        ),
        migrations.AddField(
            model_name='review',
            name='interdisciplinarity_score',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]