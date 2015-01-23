# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_remove_game_box_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='box_score_link',
            field=models.URLField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
