from __future__ import division
from django.db import models
from datetime import datetime, date, timedelta
from django.db.models import Q
from django.contrib.auth.models import User

from schedule.models import Matchup
from players.models import Player

ROSTER_SPOTS = (
	('PG', 1),('SG', 2),('SF', 3), ('PF', 4), ('C', 5),('G', 6),('F', 7),
	('UTIL', 8), ('UTIL', 9), ('UTIL', 10), ('BN', 11), ('BN', 12), ('BN', 13),
)

class Team(models.Model):
	first_name = models.CharField(max_length=15, default='Team')
	last_name = models.CharField(max_length=15, default='Name')
	owner = models.ForeignKey(User, null=True)
	wins = models.IntegerField(default=0)
	losses = models.IntegerField(default=0)
	ties = models.IntegerField(default=0)

	@property
	def record(self):
		if not self.ties:
			return "{0}-{1}".format(self.wins, self.losses)
		else:
			return "{0}-{1}-{2}".format(self.wins, self.losses, self.ties)

	@property 
	def players(self):
		return Player.objects.filter(team=self)

	def __unicode__(self):
		return "{0} {1}".format(self.first_name, self.last_name)

	@property 
	def todays_lineup(self):
		return LineUp.objects.get(team=self, date=datetime.today())

	@property
	def matchups(self):
		return Matchup.objects.filter(Q(home_team=self)|(Q(away_team=self)))

	@property
	def current_opponent(self):
		matchups = Matchup.objects.filter(Q(home_team=self)|(Q(away_team=self))) 
		matchups = matchups.filter(Q(start_date__lte=datetime.today()) & (Q(end_date__gte=datetime.today())))
		matchup = matchups[0]
		if matchup.home_team == self:
			return matchup.away_team
		return matchup.home_team

	@property
	def current_matchup(self):
		matchups = Matchup.objects.filter(Q(home_team=self)|(Q(away_team=self)))
		matchups = matchups.filter(Q(start_date__lte=datetime.today()) & (Q(end_date__gte=datetime.today())))
		matchup = matchups[0]
		return matchup

	@property
	def last_weeks_opponent(self):
		seven = timedelta(days=7)
		last_week = datetime.today() - seven
		matchups = Matchup.objects.filter(Q(home_team=self)|(Q(away_team=self)))
		matchups = matchups.filter(Q(start_date__lte=last_week))
		matchup = matchups.last()
		if matchup.home_team == self:
			return matchup.away_team
		return matchup.home_team

	@property
	def last_weeks_matchup(self):
		seven = timedelta(days=7)
		last_week = datetime.today() - seven
		matchups = Matchup.objects.filter(Q(home_team=self)|(Q(away_team=self)))
		matchups = matchups.filter(Q(start_date__lte=last_week))
		matchup = matchups.last()
		return matchup

class LineUp(models.Model):
	team = models.ForeignKey(Team)
	date = models.DateField(default='2014-10-28')
	positions = models.ManyToManyField('players.Player', through="SpotInLineup")

	@property
	def roster(self):
		return 

class SpotInLineup(models.Model):
	lineup = models.ForeignKey(LineUp)
	player = models.ForeignKey('players.Player', db_index=True)
	position = models.CharField(u'position', max_length=12, choices=ROSTER_SPOTS)


