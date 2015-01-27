from __future__ import division
from datetime import datetime, timedelta
from players.models import Player
from schedule.models import Game, StatLine

from players import utils

IGNORE_KEYS = ('name', 'nba_team', 'position')

def calculate_recent_totals(team, num_days):
	"""
	Returns a dictionary with average stats and total stats for the given time period.
	"""
	team_stats = {}
	for player in team.players:
		player_stats = utils.calculate_recent_totals(player, num_days)
		player_stats['name'] = player.name
		player_stats['nba_team'] = player.nba_team
		player_stats['position'] = player.position
		team_stats[player.id] = player_stats

	return team_stats

def calculate_recent_avgs(team_stats):
	team_averages = {}
	for k,v in team_stats.iteritems():
		if isinstance(v, dict):
			team_averages[k] = {}
			try:
				games_played = v.pop('games_played')
			except KeyError:
				continue
			if games_played == 0:
				team_averages[k]['name'] = v.get('name')
				team_averages[k]['nba_team'] = v.get('nba_team')
				team_averages[k]['position'] = v.get('position')
			if games_played > 0:
				for key, value in v.iteritems():
					if key not in IGNORE_KEYS:
						avg = value/games_played
						team_averages[k][key] = round(avg, 1)
					team_averages[k]['name'] = v.get('name')
					team_averages[k]['nba_team'] = v.get('nba_team')
					team_averages[k]['position'] = v.get('position')
				v['games_played'] = games_played

	return team_averages