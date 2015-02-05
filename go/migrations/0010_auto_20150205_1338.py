# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0009_auto_20150204_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='end',
            field=models.DateTimeField(default='2015-01-02 07:00+0500'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='start',
            field=models.DateTimeField(default='2015-01-01 22:00+0500'),
            preserve_default=True,
        ),
    ]
