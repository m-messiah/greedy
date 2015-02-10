# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0015_auto_20150206_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='duration',
            field=models.PositiveIntegerField(default=90, verbose_name='duration'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='hint1_time',
            field=models.PositiveIntegerField(default=30, verbose_name='hint1_time'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='hint2_time',
            field=models.PositiveIntegerField(default=60, verbose_name='hint2_time'),
            preserve_default=True,
        ),
    ]
