import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime
from pprint import pprint

from schedule.models import Game, NBA_TEAMS

from django.core.management.base import BaseCommand


class Command(BaseCommand):
	"""
	Scrapes the basketball reference schedule page for dates, games and teams playing
	"""
	def handle(self, *args, **options):
		# get the content of rotoworld's nba player page
		for team in NBA_TEAMS:
			url = 'http://www.basketball-reference.com/teams/{}/2015_games.html'.format(team[0])
			print('url: {}'.format(url))
			if url == 'http://www.basketball-reference.com/teams/FA/2015_games.html':
				continue

			r = requests.get(url)

			bs = BeautifulSoup(r.text)
			table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="teams_games")
			rows = table.findAll(lambda tag: tag.name=='tr')

			tipoffs = {}

			game_number = 1
			for row in rows:
				cells = row.findAll('td')
				i = 0
				for cell in cells:
					value = cell.text
					if i == 2:
						pprint('tipoff: {}'.format(value))
						tipoff = value.replace('p EST',' PM')
					if i == 5:
						if value == '@':
							tipoffs[game_number] = tipoff
							game_number += 1
		
					i += 1
			print('num of tipoffs saved for {0}: {1}'.format(team, len(tipoffs)))

			# pprint(tipoffs)
			games = Game.objects.filter(away_team=team[0]).order_by('id')
			count = 1
			for game in games:
				game.tipoff = tipoffs.get(count)
				game.save()
				print('saved game {0} with tipoff {1}'.format(game, game.tipoff))
				count += 1

