import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import date, datetime, timedelta
from dateutil import rrule

from schedule.models import Game, StatLine, Matchup
from teams.models import Team

from django.core.management.base import BaseCommand

class Command(BaseCommand):
	"""
	Generates matchups between the teams in the league from season start to season end.
	"""
	def handle(self, *args, **options):
		
		season_start = datetime(2014, 10, 28)
		season_end = datetime(2015, 4, 15)

		for dt in rrule.rrule(rrule.WEEKLY, dtstart=season_start, until=season_end):
			one_week = timedelta(days=7)
			end_date = dt + one_week
			print('generating matchups for {}'.format(dt))
			#randomize the teams in the league
			teams = Team.objects.all()
			d = {}
			i = 1
			for team in teams:
				d[i] = team.name
				i += 1

			pprint(d)

			# while j < len(teams) - 1
			# 	home = d.pop(j)
			# 	away = d.pop(-j)
			# 	print('away team: {}'.format(away))
			# 	matchup = Matchup.objects.create(home_team=home, away_team=away, start_date=dt, end_date=end_date)

