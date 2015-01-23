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
	tipoff = models.DateTimeField(auto_now=True)
	home_team = models.CharField(u'Home Team', max_length=25, choices=NBA_TEAMS)
	away_team = models.CharField(u'Away Team', max_length=25, choices=NBA_TEAMS)
	home_points = models.IntegerField(default=0)
	away_points = models.IntegerField(default=0)
	box_score_link = models.URLField(max_length=255, null=True, blank=True)

	@property
	def result(self):
		return ("{0} {1} - {2} {3}".format(self.away_team, self.away_points, self.home_points, self.home_team))

	def __unicode__(self):
		return "{0} @ {1}".format(self.away_team, self.home_team)


class BoxScore(models.Model):
	game = models.OneToOneField(Game, db_index=True)
	player = models.ForeignKey('players.Player', null=True, db_index=True)
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

