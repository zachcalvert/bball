from pprint import pprint
from datetime import date, datetime

from players.models import Player
from teams.models import Team
from teams.utils import calculate_team_totals
from schedule.models import Matchup

from django.core.management.base import BaseCommand


def prune_totals(stats):
	"""
	Remove the keys from the total stats dictionary that are unnecessary for evaluating 
	a weekly matchup
	"""
	stats.pop('fgm')
	stats.pop('fga')
	stats.pop('ftm')
	stats.pop('fta')
	stats.pop('minutes')
	stats.pop('games_played')

	return stats


class Command(BaseCommand):
	"""
	Evaluates the weeks matchups and updates team records based on stats from the last week.
	Runs once a week on Monday morning.
	"""
	def handle(self, *args, **options):
		today = datetime.today()
		matchups = Matchup.objects.filter(finalized=False).filter(end_date__lt=today)

		for matchup in matchups:
			print('Evaluating matchup {0}'.format(matchup))
			home_team_stats = calculate_team_totals(matchup.home_team, start_day=matchup.start_date, end_day = matchup.end_date)
			away_team_stats = calculate_team_totals(matchup.away_team, start_day=matchup.start_date, end_day = matchup.end_date)

			home_totals = home_team_stats.pop('totals')
			away_totals = away_team_stats.pop('totals')

			home_team_totals = prune_totals(home_totals)
			away_team_totals = prune_totals(away_totals)

			print('home_team_totals: {}'.format(home_team_totals))
			print('away_team_totals: {}'.format(away_team_totals))

			home_wins = 0
			home_losses = 0
			home_ties = 0
			away_wins = 0
			away_losses = 0
			away_ties = 0

			for k, v in home_team_totals.iteritems():
				if k == 'turnovers':
					v = -v
					t = away_team_totals[k]
					away_team_totals[k] = -t

				if v > away_team_totals[k]:
					home_wins += 1
					away_losses += 1
				elif v < away_team_totals[k]:
					home_losses += 1
					away_wins += 1
				else:
					home_ties += 1
					away_ties += 1

			print('{0} result: {1}-{2}-{3}'.format(matchup.home_team, home_wins, home_losses, home_ties))
			print('{0} result: {1}-{2}-{3}'.format(matchup.away_team, away_wins, away_losses, away_ties))

			if home_ties > 0:
				result = "{0}-{1}-{2}".format(home_wins, home_losses, home_ties)
			else:
				result = "{0}-{1}".format(home_wins, home_losses) 

			# save the matchup
			matchup.result = result
			matchup.finalized = True
			matchup.save()

			# save the respective teams records
			matchup.home_team.wins += home_wins
			matchup.home_team.losses += home_losses
			matchup.home_team.ties += home_ties
			matchup.home_team.save()
			print("saved {0} with new record: {1}".format(matchup.home_team, matchup.home_team.record))


			matchup.away_team.wins += away_wins
			matchup.away_team.losses += away_losses
			matchup.away_team.ties += away_ties
			matchup.away_team.save()
			print("saved {0} with new record: {1}".format(matchup.away_team, matchup.away_team.record))


