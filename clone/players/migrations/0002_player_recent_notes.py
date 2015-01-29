# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='recent_notes',
            field=models.CharField(default=b'No recent notes.', max_length=500),
            preserve_default=True,
        ),
    ]
