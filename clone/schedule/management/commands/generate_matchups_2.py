from datetime import date, datetime, timedelta
from dateutil import rrule
import operator
import copy

from schedule.models import Game, StatLine, Matchup
from teams.models import Team

from django.core.management.base import BaseCommand

def fixtures(teams):
	    if len(teams) % 2:
	        teams.append('Day off')  # if team number is odd - use 'day off' as fake team     

	    rotation = list(teams)       # copy the list

	    fixtures = []
	    for i in range(0, len(teams)-1):
	        fixtures.append(rotation)
	        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]

	    return fixtures

class Command(BaseCommand):
	"""
	Generates matchups between the teams in the league from season start to season end.
	"""
	def handle(self, *args, **options):
		
		season_start = datetime(2014, 10, 28)
		season_end = datetime(2015, 4, 15)

		team_names = []
		for team in Team.objects.all():
			team_names.append(team.name)

		all_matches = fixtures(team_names)

		i = 0
		for dt in rrule.rrule(rrule.WEEKLY, dtstart=season_start, until=season_end):
			print('\ncreating matchups for week {}:'.format(dt))
			one_week = timedelta(days=7)
			end_date = dt + one_week

			try:
				matches = all_matches[i]
			except IndexError:
				# first round over, create a new round of reverse fixtures
				i = 0
				reverse_teams =  [list(x) for x in zip(team_names[1::2], team_names[::2])]
				reverse_teams = reduce(operator.add,  reverse_teams)
				all_matches = fixtures(reverse_teams)
				matches = all_matches[i]

			while matches:
				away = matches.pop(0)
				home = matches.pop(0)
				home_team = Team.objects.get(name=home)
				away_team = Team.objects.get(name=away)
				Matchup.objects.create(home_team=home_team, away_team=away_team, start_date=dt, end_date=end_date)
				print('added matchup between {0} and {1}'.format(home_team, away_team))

			i += 1

