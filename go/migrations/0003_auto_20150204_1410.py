# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0002_auto_20150204_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_hint1',
            new_name='hint1',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_hint2',
            new_name='hint2',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_num',
            new_name='num',
        ),
    ]
