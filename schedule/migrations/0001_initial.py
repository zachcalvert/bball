# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('tipoff', models.CharField(max_length=8, null=True, blank=True)),
                ('home_team', models.CharField(max_length=25, verbose_name='Home Team', choices=[(b'ATL', b'Atlanta Hawks'), (b'BRK', b'Brooklyn Nets'), (b'BOS', b'Boston Celtics'), (b'CHO', b'Charlotte Hornets'), (b'CHI', b'Chicago Bulls'), (b'CLE', b'Cleveland Cavaliers'), (b'DAL', b'Dallas Mavericks'), (b'DEN', b'Denver Nuggets'), (b'DET', b'Detroit Pistons'), (b'GSW', b'Golden State Warriors'), (b'HOU', b'Houston Rockets'), (b'IND', b'Indiana Pacers'), (b'LAC', b'Los Angeles Clippers'), (b'LAL', b'Los Angeles Lakers'), (b'MEM', b'Memphis Grizzlies'), (b'MIA', b'Miami Heat'), (b'MIN', b'Minnesota Timberwolves'), (b'MIL', b'Milwaukee Bucks'), (b'NOP', b'New Orleans Pelicans'), (b'NYK', b'New York Knicks'), (b'OKC', b'Oklahoma City Thunder'), (b'ORL', b'Orlando Magic'), (b'PHI', b'Philadelphia 76ers'), (b'PHO', b'Phoenix Suns'), (b'POR', b'Portland TrailBlazers'), (b'SAS', b'San Antonio Spurs'), (b'SAC', b'Sacramento Kings'), (b'TOR', b'Toronto Raptors'), (b'UTA', b'Utah Jazz'), (b'WAS', b'Washington Wizards'), (b'FA', b'Free Agent')])),
                ('away_team', models.CharField(max_length=25, verbose_name='Away Team', choices=[(b'ATL', b'Atlanta Hawks'), (b'BRK', b'Brooklyn Nets'), (b'BOS', b'Boston Celtics'), (b'CHO', b'Charlotte Hornets'), (b'CHI', b'Chicago Bulls'), (b'CLE', b'Cleveland Cavaliers'), (b'DAL', b'Dallas Mavericks'), (b'DEN', b'Denver Nuggets'), (b'DET', b'Detroit Pistons'), (b'GSW', b'Golden State Warriors'), (b'HOU', b'Houston Rockets'), (b'IND', b'Indiana Pacers'), (b'LAC', b'Los Angeles Clippers'), (b'LAL', b'Los Angeles Lakers'), (b'MEM', b'Memphis Grizzlies'), (b'MIA', b'Miami Heat'), (b'MIN', b'Minnesota Timberwolves'), (b'MIL', b'Milwaukee Bucks'), (b'NOP', b'New Orleans Pelicans'), (b'NYK', b'New York Knicks'), (b'OKC', b'Oklahoma City Thunder'), (b'ORL', b'Orlando Magic'), (b'PHI', b'Philadelphia 76ers'), (b'PHO', b'Phoenix Suns'), (b'POR', b'Portland TrailBlazers'), (b'SAS', b'San Antonio Spurs'), (b'SAC', b'Sacramento Kings'), (b'TOR', b'Toronto Raptors'), (b'UTA', b'Utah Jazz'), (b'WAS', b'Washington Wizards'), (b'FA', b'Free Agent')])),
                ('home_points', models.IntegerField(default=0)),
                ('away_points', models.IntegerField(default=0)),
                ('boxscore_link', models.URLField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('week', models.IntegerField(default=22)),
                ('finalized', models.BooleanField(default=False)),
                ('result', models.CharField(max_length=10, null=True, blank=True)),
                ('away_team', models.ForeignKey(related_name='away team', to='teams.Team')),
                ('home_team', models.ForeignKey(related_name='home team', to='teams.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StatLine',
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
                ('added_to_player', models.BooleanField(default=False)),
                ('game', models.ForeignKey(to='schedule.Game')),
                ('player', models.ForeignKey(to='players.Player')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='stat_lines',
            field=models.ManyToManyField(to='players.Player', through='schedule.StatLine'),
            preserve_default=True,
        ),
    ]
