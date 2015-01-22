from __future__ import division
from django.db import models
import django_tables2 as tables

from players.models import Player

class Team(models.Model):
	name = models.CharField(max_length=30, unique=True)
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
		return self.name


	@property
	def points(self):
		points = 0
		for player in self.players:
			points += player.points
		return points

	@property
	def assists(self):
		assists = 0
		for player in self.players:
			assists += player.assists
		return assists

	@property
	def rebounds(self):
		rebounds = 0
		for player in self.players:
			rebounds += player.rebounds
		return rebounds

	@property
	def steals(self):
		steals = 0
		for player in self.players:
			steals += player.steals
		return steals

	@property
	def blocks(self):
		blocks = 0
		for player in self.players:
			blocks += player.blocks
		return blocks

	@property
	def threes(self):
		threes = 0
		for player in self.players:
			threes += player.threes
		return threes

	@property
	def turnovers(self):
		turnovers = 0
		for player in self.players:
			turnovers += player.turnovers
		return turnovers

	@property
	def fgm(self):
		fgm = 0
		for player in self.players:
			fgm += player.fgm
		return fgm

	@property
	def fga(self):
		fga = 0
		for player in self.players:
			fga += player.fga
		return fga

	@property
	def fgpct(self):
		fgpct = self.fgm/self.fga
		return round(fgpct, 4) * 100

	@property
	def ftm(self):
		ftm = 0
		for player in self.players:
			ftm += player.ftm
		return ftm

	@property
	def fta(self):
		fta = 0
		for player in self.players:
			fta += player.fta
		return fta

	@property
	def ftpct(self):
		ftpct = self.ftm/self.fta
		return round(ftpct, 4) * 100



