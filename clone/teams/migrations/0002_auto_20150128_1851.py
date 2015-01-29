# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineUp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.datetime(2015, 1, 28, 18, 51, 18, 992415))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpotInLineup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=12, verbose_name='position', choices=[(b'PG', 1), (b'SG', 2), (b'SF', 3), (b'PF', 4), (b'C', 5), (b'G', 6), (b'F', 7), (b'UTIL', 8), (b'UTIL', 9), (b'UTIL', 10), (b'BN', 11), (b'BN', 12), (b'BN', 13)])),
                ('lineup', models.ForeignKey(to='teams.LineUp')),
                ('player', models.ForeignKey(to='players.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='lineup',
            name='positions',
            field=models.ManyToManyField(to='players.Player', through='teams.SpotInLineup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lineup',
            name='team',
            field=models.ForeignKey(to='teams.Team'),
            preserve_default=True,
        ),
    ]
