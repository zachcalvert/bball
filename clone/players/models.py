from __future__ import division
from django.db import models
import django_tables2 as tables

NBA_TEAMS = (
	('ATL', 'Atlanta Hawks'),('BRK', 'Brooklyn Nets'),('BOS', 'Boston Celtics'),
	('CHO', 'Charlotte Hornets'),('CHI', 'Chicago Bulls'),('CLE', 'Cleveland Cavaliers'),
	('DAL', 'Dallas Mavericks'),('DEN', 'Denver Nuggets'),('DET', 'Detroit Pistons'),
	('GSW', 'Golden State Warriors'),('HOU', 'Houston Rockets'),('IND', 'Indiana Pacers'),
	('LAC', 'Los Angeles Clippers'),('LAL', 'Los Angeles Lakers'),('MEM', 'Memphis Grizzlies'),
	('MIA', 'Miami Heat'),('MIN', 'Minnesota Timberwolves'),('MIL', 'Milwaukee Bucks'),
	('NOP', 'New Orleans Pelicans'),('NYK', 'New York Knicks'),('OKC', 'Oklahoma City Thunder'),
	('ORL', 'Orlando Magic'),('PHI', 'Philadelphia 76ers'),('PHO', 'Phoenix Suns'),
	('POR', 'Portland TrailBlazers'),('SAS', 'San Antonio Spurs'),('SAC', 'Sacramento Kings'),
	('TOR', 'Toronto Raptors'),('UTA', 'Utah Jazz'),('WAS', 'Washington Wizards'),('FA', 'Free Agent'),
)

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
	#attributes
	name = models.CharField(max_length=35)
	team = models.ForeignKey('teams.Team', null=True, blank=True)
	position = models.CharField(u'Position', choices=POSITIONS, default='PG', max_length=15)
	nba_team = models.CharField(u'NBA Team', choices=NBA_TEAMS, default='FA', max_length=25)

	#stats
	games = models.IntegerField(default=0)
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

	@property
	def ppg(self):
		if self.games == 0:
			return 0
		ppg = self.points/self.games
		return round(ppg, 1)

	@property
	def apg(self):
		if self.games == 0:
			return 0
		apg = self.assists/self.games
		return round(apg, 1)

	@property
	def rpg(self):
		if self.games == 0:
			return 0
		rpg = self.rebounds/self.games
		return round(rpg, 1)

	@property
	def bpg(self):
		if self.games == 0:
			return 0
		bpg = self.blocks/self.games
		return round(bpg, 1)

	@property
	def spg(self):
		if self.games == 0:
			return 0
		spg = self.steals/self.games
		return round(spg, 1)

	@property
	def threespg(self):
		if self.games == 0:
			return 0
		threespg = self.threes/self.games
		return round(threespg, 1)

	@property
	def mpg(self):
		if self.games == 0:
			return 0
		mpg = self.minutes/self.games
		return round(mpg, 1)

	@property
	def fgpct(self):
		fgpct = self.fgm/self.fga
		return round(fgpct, 4) * 100

	@property
	def ftpct(self):
		ftpct = self.ftm/self.fta
		return round(ftpct, 4) * 100

	def __unicode__(self):
		return self.name


class PlayerTable(tables.Table):
	class Meta:
		model = Player
		exclude = ("id","team",)
		sequence = ("name", "position", "nba_team", "games", "minutes",)
		attrs = {"class": "paleblue"}

