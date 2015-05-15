from __future__ import division

from players import utils

IGNORE_KEYS = ('name', 'nba_team', 'position')

def calculate_team_totals(team, start_day, end_day):
	"""
	Returns a dictionary with average stats and total stats for the given time period.
	"""
	team_stats = {}
	team_stats['totals'] = {"games_played": 0, "minutes": 0, "fgm": 0, "fga": 0, "ftm": 0, "fta": 0, 
		"threes": 0, "rebounds": 0, "assists": 0, "steals": 0, "blocks": 0, "turnovers": 0, "points": 0,
		"fgpct": .0, "ftpct": .0} 
	for player in team.players:
		player_stats = utils.calculate_totals(player, start_day, end_day)
		for k, v in player_stats.iteritems():
			team_stats['totals'][k] += v
		# we need to render these 'non-stat' attributes 
		player_stats['name'] = player.name
		player_stats['nba_team'] = player.nba_team
		player_stats['position'] = player.position
		team_stats[player.id] = player_stats

	try:
		team_stats['totals']['fgpct'] = round(team_stats['totals'].get('fgm')/team_stats['totals'].get('fga'), 3)
	except ZeroDivisionError:
		team_stats['totals']['fgpct'] = .000
	try:
		team_stats['totals']['ftpct'] = round(team_stats['totals'].get('ftm')/team_stats['totals'].get('fta'), 3)
	except ZeroDivisionError:
		team_stats['totals']['ftpct'] = .000

	return team_stats

def calculate_team_avgs(team_stats):
	team_averages = {}
	for k,v in team_stats.iteritems():
		if isinstance(v, dict):
			team_averages[k] = {}
			try:
				games_played = v.pop('games_played')
			except KeyError:
				continue
			team_averages[k]['name'] = v.get('name')
			team_averages[k]['nba_team'] = v.get('nba_team')
			team_averages[k]['position'] = v.get('position')

			for key, value in v.iteritems():
				if key not in IGNORE_KEYS:
					if games_played == 0:
						avg = 0
					else:
						avg = value/games_played
					team_averages[k][key] = round(avg, 1)
				team_averages[k]['fgpct'] = v.get('fgpct')
				team_averages[k]['ftpct'] = v.get('ftpct')
			v['games_played'] = games_played

	return team_averages