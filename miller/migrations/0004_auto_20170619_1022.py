# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 10:22
from __future__ import unicode_literals

import django.contrib.postgres.indexes
from django.db import migrations
from django.contrib.postgres.operations import BtreeGinExtension

class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0003_ngrams'),
    ]

    operations = [
        BtreeGinExtension(),
        migrations.AlterModelOptions(
            name='ngrams',
            options={'verbose_name_plural': 'a lot of ngrams'},
        ),
        migrations.AddIndex(
            model_name='ngrams',
            index=django.contrib.postgres.indexes.GinIndex(fields=[b'segment'], name='miller_ngra_segment_511b9b_gin'),
        ),
    ]