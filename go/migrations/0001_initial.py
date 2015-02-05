# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(max_length=100)),
                ('weight', models.SmallIntegerField()),
                ('posted', models.BooleanField()),
                ('time_posted', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('task_num', models.SmallIntegerField()),
                ('task_desc', models.TextField()),
                ('task_hint1', models.TextField(default='-')),
                ('task_hint2', models.TextField(default='-')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='code',
            name='task',
            field=models.ForeignKey(to='go.Task'),
            preserve_default=True,
        ),
    ]
