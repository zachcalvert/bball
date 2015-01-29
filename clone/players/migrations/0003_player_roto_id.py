# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_player_recent_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='roto_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
