# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_player_roto_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='recent_notes',
            new_name='recent_report_0',
        ),
    ]
