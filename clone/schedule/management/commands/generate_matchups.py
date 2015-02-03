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

		for team in Team.objects.filter(name='Stairway to Kevin'):
			opponents = list(Team.objects.all().exclude(name=team.name))

			i = 0	
			for dt in rrule.rrule(rrule.WEEKLY, dtstart=season_start, until=season_end):
				one_week = timedelta(days=7)
				end_date = dt + one_week
				print('generating matchup for {}'.format(dt))
				
				if i % 2 == 0:
					home = team
					away = opponents[i]
				else:
					away = team
					home = opponents[i]
					
				matchup = Matchup.objects.create(home_team=home, away_team=away, start_date=dt, end_date=end_date)
				print('created matchup between {0} and {1}'.format(home, away))
				i += 1
				if i > len(opponents) - 1:
					i = 0



