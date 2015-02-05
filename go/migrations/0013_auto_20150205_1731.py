# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0012_auto_20150205_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='tools',
            field=models.TextField(default='Automobile\nInternet device\nFlashlight'),
            preserve_default=True,
        ),
    ]
