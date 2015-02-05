# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0007_auto_20150204_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='anons',
            new_name='prikvel',
        ),
    ]
