# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_matchup'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchup',
            name='week',
            field=models.IntegerField(default=22),
            preserve_default=True,
        ),
    ]
