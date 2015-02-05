# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0003_auto_20150204_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='code',
            old_name='time_posted',
            new_name='post_time',
        ),
    ]
