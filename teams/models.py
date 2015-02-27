from __future__ import division
from django.db import models
from datetime import datetime, date, timedelta
from django.db.models import Q, Max
from django.contrib.auth.models import User

from players.models import Player
from schedule.models import Matchup

class Team(models.Model):
	first_name = models.CharField(max_length=15, default='Team')
	last_name = models.CharField(max_length=15, default='Name')
	owner = models.ForeignKey(User, null=True)
	wins = models.IntegerField(default=0)
	losses = models.IntegerField(default=0)
	ties = models.IntegerField(default=0)

	class Meta:
           ordering = ['-wins', 'losses']

	def __unicode__(self):
		return "{0} {1}".format(self.first_name, self.last_name)

	@property
	def record(self):
		if not self.ties:
			return "{0}-{1}".format(self.wins, self.losses)
		else:
			return "{0}-{1}-{2}".format(self.wins, self.losses, self.ties)

	@property 
	def players(self):
		return Player.objects.filter(team=self)

	@property
	def matchups(self):
		return Matchup.objects.filter(Q(home_team=self)|(Q(away_team=self))).order_by('week')

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

	@property
	def standing(self):
		teams = Team.objects.all()
		teams = list(teams)
		# because first place has index of 0
		return teams.index(self) + 1

	@property
	def games_behind(self):
		max_wins = Team.objects.all().aggregate(Max('wins'))
		first_place = Team.objects.get(wins=max_wins['wins__max'])

		if self == first_place:
			return '--'
		else:
			return ((first_place.wins - self.wins) + (first_place.losses - self.losses)/2)
