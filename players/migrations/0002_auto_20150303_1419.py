# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['-ppg']},
        ),
        migrations.AddField(
            model_name='player',
            name='apg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='bpg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='fgapg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='fgmpg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='ftapg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='ftmpg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='mpg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='ppg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='rpg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='spg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='threespg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='topg',
            field=models.DecimalField(default=Decimal('0.0'), max_digits=6, decimal_places=1),
            preserve_default=True,
        ),
    ]
