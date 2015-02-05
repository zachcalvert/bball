from django import template
from datetime import date, timedelta

from players.models import Player
from players.utils import todays_opponent, todays_game_status

register = template.Library()

@register.filter(name='get_todays_opponent')
def get_todays_opponent(value):
	r = todays_opponent(value) 
	if r is not None:
		return r
	else:
		return ''

@register.filter(name='get_tipoff')
def get_tipoff(value):
	r = todays_game_status(value)
	if r is not None:
		return r
	else:
		return ''

@register.filter(name='format_pct')
def format_pct(value):
	retval = str(value)
	retval = retval.replace('0','')
	while len(retval) < 4:
		retval += '0'
	return retval


@register.filter(name='total_team_games')
def total_team_games(value):
	total_games = 0
	for player_id in value.iteritems():
		player_games = player_id[1].get('games_played')
		total_games += player_games
	return total_games


@register.filter(name='total_team_minutes')
def total_team_minutes(value):
	total_minutes = 0
	for player_id in value.iteritems():
		player_minutes = player_id[1].get('minutes')
		total_minutes += player_minutes
	return total_minutes