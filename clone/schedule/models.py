from django.db import models

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

class Season(models.Model):
	pass

class Game(models.Model):
	date = models.DateField(auto_now=False)
	tipoff = models.CharField(max_length=8, null=True, blank=True)
	home_team = models.CharField(u'Home Team', max_length=25, choices=NBA_TEAMS)
	away_team = models.CharField(u'Away Team', max_length=25, choices=NBA_TEAMS)
	home_points = models.IntegerField(default=0)
	away_points = models.IntegerField(default=0)
	boxscore_link = models.URLField(max_length=255, null=True, blank=True)
	stat_lines = models.ManyToManyField('players.Player', through="StatLine")

	@property
	def result(self):
		return ("{0} {1} - {2} {3}".format(self.away_team, self.away_points, self.home_points, self.home_team))

	def __unicode__(self):
		return "{0}: {1} @ {2}".format(self.date, self.away_team, self.home_team)


class StatLine(models.Model):
	game = models.ForeignKey(Game, db_index=True)
	player = models.ForeignKey('players.Player', db_index=True)
	mp = models.CharField(max_length=5, null=True, blank=True)
	fgm = models.IntegerField(default=0)
	fga = models.IntegerField(default=0)
	ftm = models.IntegerField(default=0)
	fta = models.IntegerField(default=0)
	threesm = models.IntegerField(default=0)
	threesa = models.IntegerField(default=0)
	orbs = models.IntegerField(default=0)
	drbs = models.IntegerField(default=0)
	trbs = models.IntegerField(default=0)
	asts = models.IntegerField(default=0)
	stls = models.IntegerField(default=0)
	blks = models.IntegerField(default=0)
	tos = models.IntegerField(default=0)
	pfs = models.IntegerField(default=0)
	pts = models.IntegerField(default=0)
	added_to_player = models.BooleanField(default=False)

	def __unicode__(self):
		return "Box Score for {}".format(self.game)

class Matchup(models.Model):
	home_team = models.ForeignKey('teams.Team', related_name='home team')
	away_team = models.ForeignKey('teams.Team', related_name='away team')
	start_date = models.DateField(auto_now=False)
	end_date = models.DateField(auto_now=False)


