# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_auto_20150130_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='recent_report_0',
        ),
        migrations.AddField(
            model_name='player',
            name='recent_notes',
            field=models.CharField(default=b'No recent notes.', max_length=2000),
            preserve_default=True,
        ),
    ]
