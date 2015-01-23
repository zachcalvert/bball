# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20150122_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='box_score',
        ),
    ]
