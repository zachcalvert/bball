from __future__ import division
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
