# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20150122_2226'),
        ('schedule', '0002_auto_20150122_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoxScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mp', models.CharField(max_length=5, null=True, blank=True)),
                ('fgm', models.IntegerField(default=0)),
                ('fga', models.IntegerField(default=0)),
                ('ftm', models.IntegerField(default=0)),
                ('fta', models.IntegerField(default=0)),
                ('threesm', models.IntegerField(default=0)),
                ('threesa', models.IntegerField(default=0)),
                ('orbs', models.IntegerField(default=0)),
                ('drbs', models.IntegerField(default=0)),
                ('trbs', models.IntegerField(default=0)),
                ('asts', models.IntegerField(default=0)),
                ('stls', models.IntegerField(default=0)),
                ('blks', models.IntegerField(default=0)),
                ('tos', models.IntegerField(default=0)),
                ('pfs', models.IntegerField(default=0)),
                ('pts', models.IntegerField(default=0)),
                ('game', models.OneToOneField(to='schedule.Game')),
                ('player', models.ForeignKey(to='players.Player', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='box_score',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
