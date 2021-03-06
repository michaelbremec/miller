# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-25 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0011_auto_20160418_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[(b'bibtex', b'bibtex'), (b'video-cover', b'video interview'), (b'video', b'video'), (b'text', b'text'), (b'picture', b'picture'), (b'pdf', b'pdf'), (b'image', b'picture')], max_length=24),
        ),
        migrations.AlterField(
            model_name='story',
            name='documents',
            field=models.ManyToManyField(blank=True, related_name='documents', through='miller.Caption', to='miller.Document'),
        ),
    ]
