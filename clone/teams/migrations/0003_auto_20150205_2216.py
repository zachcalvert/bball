# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0002_auto_20150130_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
        migrations.AddField(
            model_name='team',
            name='first_name',
            field=models.CharField(default=b'Team', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='last_name',
            field=models.CharField(default=b'Name', max_length=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='team',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
