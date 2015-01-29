# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20150128_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineup',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 1, 29, 20, 43, 30, 548142)),
            preserve_default=True,
        ),
    ]
