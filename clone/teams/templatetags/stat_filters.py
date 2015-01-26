from django import template
from datetime import date, timedelta

from players.models import Player
from players.utils import todays_opponent

register = template.Library()

@register.filter(name='get_average')
def get_average(value):
	arg_list = [value.strip() for arg in value.split(',')]
	total = int(arg_list[0])
	games = int(arg_list[1])
	return total/games

@register.filter(name='get_todays_opponent')
def get_todays_opponent(value):
	r = todays_opponent(value) 
	if r is not None:
		return r
	else:
		return ''
