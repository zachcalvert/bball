# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='tipoff',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
