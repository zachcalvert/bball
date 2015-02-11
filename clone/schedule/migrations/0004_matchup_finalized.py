# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_matchup_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchup',
            name='finalized',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
