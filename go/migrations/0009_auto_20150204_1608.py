# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0008_auto_20150204_1554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='date',
            new_name='start',
        ),
        migrations.AddField(
            model_name='game',
            name='end',
            field=models.DateTimeField(default='2015-01-01 07:00'),
            preserve_default=False,
        ),
    ]
