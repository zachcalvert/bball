# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20150303_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='fgpct',
            field=models.DecimalField(default=Decimal('0.000'), max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='ftpct',
            field=models.DecimalField(default=Decimal('0.000'), max_digits=6, decimal_places=3),
            preserve_default=True,
        ),
    ]
