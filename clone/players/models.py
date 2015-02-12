from __future__ import division
from django.db import models
from django.db.models import Q
from datetime import datetime, timedelta

from schedule.models import Game, StatLine, NBA_TEAMS

POSITIONS = (
	('PG', 'Point Guard'),
	('SG', 'Shooting Guard'),
	('SF', 'Small Forward'),
	('PF', 'Power Forward'),
	('C', 'Center'),
)

class Player(models.Model):
	"""
	A simple model describing an NBA player that may be on one Team.
	"""
	# attributes
	name = models.CharField(max_length=35)
	team = models.ForeignKey('teams.Team', null=True, blank=True)
	position = models.CharField(u'Position', choices=POSITIONS, default='PG', max_length=15)
	nba_team = models.CharField(u'NBA Team', choices=NBA_TEAMS, default='FA', max_length=25)

	# stats
	games_played = models.IntegerField(default=0)
	minutes = models.IntegerField(default=0)
	fgm = models.IntegerField(default=0)
	fga = models.IntegerField(default=0)
	ftm = models.IntegerField(default=0)
	fta = models.IntegerField(default=0)
	points = models.IntegerField(default = 0)
	threes = models.IntegerField(default = 0)
	rebounds = models.IntegerField(default = 0)
	assists = models.IntegerField(default = 0)
	steals = models.IntegerField(default = 0)
	blocks = models.IntegerField(default = 0)
	turnovers = models.IntegerField(default = 0)

	# notes
	roto_id = models.IntegerField(default=0)
	recent_notes = models.CharField(max_length=2000, default='No recent notes.')

	class Meta:
		ordering = ['-points']

	@property
	def recent_statlines(self):
		now = datetime.now()
		today = now.date()
		delta = timedelta(days=10)
		timespan = today - delta
		return StatLine.objects.filter(player_id=self.id, game__date__gte=timespan)

	@property 
	def upcoming_games(self):
		now = datetime.now()
		today = now.date()
		delta = timedelta(days=10)
		timespan = today + delta
		games = Game.objects.filter(Q(home_team=self.nba_team)| Q(away_team=self.nba_team), date__gte=today, date__lte=timespan)
		return games

	@property
	def games(self):
		games = Game.objects.filter(Q(home_team=self.nba_team)| Q(away_team=self.nba_team))


	def __unicode__(self):
		return self.name

