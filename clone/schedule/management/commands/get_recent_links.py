import requests
from bs4 import BeautifulSoup
from datetime import datetime

from schedule.models import Game

from django.core.management.base import BaseCommand
from django.core.management import call_command

def fetch_statlines(game):

call_command('my_command', 'foo', bar='baz')

class Command(BaseCommand):
	"""
	Scrapes the box scores on basketball reference and loads the relevant stats 
	for use in the app
	"""
	def handle(self, *args, **options):

		now = datetime.now()
		today = now.date()

		games = Game.objects.filter(boxscore_link='', date__lt=today)

		for game in games:
			string = game.date.strftime('%m/%d/%Y')
			year = string[6:]
			day = string[3:5]
			month = string[:2]
			url = "boxscores/{0}{1}{2}0{3}.html".format(year, month, day, game.home_team)
			game.boxscore_link = url
			game.save()

		call_command('get_boxscores', games=games)
		