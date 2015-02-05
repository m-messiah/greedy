# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0013_auto_20150205_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_bonus',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
