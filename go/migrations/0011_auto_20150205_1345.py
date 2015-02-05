# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0010_auto_20150205_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 2, 7, 0)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 1, 22, 0)),
            preserve_default=True,
        ),
    ]
