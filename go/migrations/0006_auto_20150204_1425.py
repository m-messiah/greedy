# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0005_auto_20150204_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='post_time',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
