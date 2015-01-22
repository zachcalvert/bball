# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=35)),
                ('position', models.CharField(default=b'PG', max_length=15, verbose_name='Position', choices=[(b'PG', b'Point Guard'), (b'SG', b'Shooting Guard'), (b'SF', b'Small Forward'), (b'PF', b'Power Forward'), (b'C', b'Center')])),
                ('nba_team', models.CharField(default=b'FA', max_length=25, verbose_name='NBA Team', choices=[(b'ATL', b'Atlanta Hawks'), (b'BRK', b'Brooklyn Nets'), (b'BOS', b'Boston Celtics'), (b'CHO', b'Charlotte Hornets'), (b'CHI', b'Chicago Bulls'), (b'CLE', b'Cleveland Cavaliers'), (b'DAL', b'Dallas Mavericks'), (b'DEN', b'Denver Nuggets'), (b'DET', b'Detroit Pistons'), (b'GSW', b'Golden State Warriors'), (b'HOU', b'Houston Rockets'), (b'IND', b'Indiana Pacers'), (b'LAC', b'Los Angeles Clippers'), (b'LAL', b'Los Angeles Lakers'), (b'MEM', b'Memphis Grizzlies'), (b'MIA', b'Miami Heat'), (b'MIN', b'Minnesota Timberwolves'), (b'MIL', b'Milwaukee Bucks'), (b'NOP', b'New Orleans Pelicans'), (b'NYK', b'New York Knicks'), (b'OKC', b'Oklahoma City Thunder'), (b'ORL', b'Orlando Magic'), (b'PHI', b'Philadelphia 76ers'), (b'PHO', b'Phoenix Suns'), (b'POR', b'Portland TrailBlazers'), (b'SAS', b'San Antonio Spurs'), (b'SAC', b'Sacramento Kings'), (b'TOR', b'Toronto Raptors'), (b'UTA', b'Utah Jazz'), (b'WAS', b'Washington Wizards'), (b'FA', b'Free Agent')])),
                ('games', models.IntegerField(default=0)),
                ('minutes', models.IntegerField(default=0)),
                ('fgm', models.IntegerField(default=0)),
                ('fga', models.IntegerField(default=0)),
                ('ftm', models.IntegerField(default=0)),
                ('fta', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('threes', models.IntegerField(default=0)),
                ('rebounds', models.IntegerField(default=0)),
                ('assists', models.IntegerField(default=0)),
                ('steals', models.IntegerField(default=0)),
                ('blocks', models.IntegerField(default=0)),
                ('turnovers', models.IntegerField(default=0)),
                ('team', models.ForeignKey(blank=True, to='teams.Team', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
