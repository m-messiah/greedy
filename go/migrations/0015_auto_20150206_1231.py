# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('go', '0014_task_is_bonus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='code',
            field=models.CharField(verbose_name='code', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='code',
            name='is_posted',
            field=models.BooleanField(verbose_name='posted', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='code',
            name='post_time',
            field=models.DateTimeField(verbose_name='post_time', auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='code',
            name='task',
            field=models.ForeignKey(to='go.Task', verbose_name='task'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='code',
            name='weight',
            field=models.SmallIntegerField(verbose_name='weight'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='author',
            field=models.CharField(verbose_name='author', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='end',
            field=models.DateTimeField(verbose_name='end', default=datetime.datetime(2015, 1, 2, 7, 0)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='legend',
            field=models.TextField(verbose_name='legend'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(verbose_name='name', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='pretask',
            field=models.TextField(verbose_name='pretask'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='start',
            field=models.DateTimeField(verbose_name='start', default=datetime.datetime(2015, 1, 1, 22, 0)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='game',
            name='tools',
            field=models.TextField(verbose_name='tools', default='Automobile\nInternet device\nFlashlight'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='desc',
            field=models.TextField(verbose_name='text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='game',
            field=models.ForeignKey(to='go.Game', verbose_name='game'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='hint1',
            field=models.TextField(verbose_name='hint1', default='-'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='hint2',
            field=models.TextField(verbose_name='hint2', default='-'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='is_bonus',
            field=models.BooleanField(verbose_name='is_bonus', default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='num',
            field=models.SmallIntegerField(verbose_name='num'),
            preserve_default=True,
        ),
    ]
