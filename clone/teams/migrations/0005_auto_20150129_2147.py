# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20150129_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineup',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 1, 29, 21, 47, 36, 507083)),
            preserve_default=True,
        ),
    ]
