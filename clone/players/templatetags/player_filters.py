from django import template
from datetime import date, timedelta

from players.models import Player
from players.utils import todays_opponent, todays_game_status

register = template.Library()

@register.filter(name='get_todays_opponent')
def get_todays_opponent(value):