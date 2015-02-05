# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0011_auto_20150205_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='prikvel',
            new_name='pretask',
        ),
        migrations.AddField(
            model_name='game',
            name='tools',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
