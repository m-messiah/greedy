# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='posted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
