# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20150130_0104'),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('away_team', models.ForeignKey(related_name='away team', to='teams.Team')),
                ('home_team', models.ForeignKey(related_name='home team', to='teams.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
