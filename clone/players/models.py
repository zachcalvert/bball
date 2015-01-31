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
	def ppg(self):
		if self.games_played == 0:
			return 0
		ppg = self.points/self.games_played
		return round(ppg, 1)

	@property
	def apg(self):
		if self.games_played == 0:
			return 0
		apg = self.assists/self.games_played
		return round(apg, 1)

	@property
	def rpg(self):
		if self.games_played == 0:
			return 0
		rpg = self.rebounds/self.games_played
		return round(rpg, 1)

	@property
	def bpg(self):
		if self.games_played == 0:
			return 0
		bpg = self.blocks/self.games_played
		return round(bpg, 1)

	@property
	def spg(self):
		if self.games_played == 0:
			return 0
		spg = self.steals/self.games_played
		return round(spg, 1)

	@property
	def threespg(self):
		if self.games_played == 0:
			return 0
		threespg = self.threes/self.games_played
		return round(threespg, 1)

	@property
	def mpg(self):
		if self.games_played == 0:
			return 0
		mpg = self.minutes/self.games_played
		return round(mpg, 1)

	@property
	def fgpct(self):
		fgpct = self.fgm/self.fga
		return round(fgpct, 4) * 100

	@property
	def ftpct(self):
		ftpct = self.ftm/self.fta
		return round(ftpct, 4) * 100

	@property
	def topg(self):
		if self.games_played == 0:
			return 0
		topg = self.turnovers/self.games_played
		return round(topg, 1)

	@property
	def games(self):
		games = Game.objects.filter(Q(home_team=self.nba_team)| Q(away_team=self.nba_team))


	def __unicode__(self):
		return self.name

