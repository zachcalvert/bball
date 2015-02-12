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

@register.filter(name='format_date')
def format_date(value):
	days = ((0,'Sun'), 
            (1,'Mon'), 
            (2,'Tue'), 
            (3,'Wed'), 
            (4,'Thu'),  
            (5,'Fri'), 
            (6, 'Sat'),)
	date_object = value.date
	weekday = date_object.weekday()
	tup = days[weekday]
	day = tup[1]

	return '{0} {1} - {2}'.format(day, date_object.strftime('%b %d, %Y'), value.tipoff)


@register.filter(name='format_standing')
def format_standing(value):
	if value == 1:
		return '1st'
	elif value == 2:
		return '2nd'
	elif value == 3:
		return '3rd'
	elif value == 4:
		return '4th'
	elif value == 5:
		return '5th'
	elif value == 6:
		return '6th'
	elif value == 7:
		return '7th'
	elif value == 8:
		return '8th'
	elif value == 9:
		return '9th'
	elif value == 10:
		return '10th'
	elif value == 11:
		return '11th'
	elif value == 12:
		return '12th'
