# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0004_auto_20150204_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='code',
            old_name='posted',
            new_name='is_posted',
        ),
    ]
