from__future__ import division
from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter(name='get_average')
def get_average(value):
	arg_list = [value.strip() for arg in value.split(',')]
	total = int(arg_list[0])
	games = int(arg_list[1])
	return total/games