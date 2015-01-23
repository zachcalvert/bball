import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime

from schedule.models import Game

from django.core.management.base import BaseCommand

class Command(BaseCommand):
	"""
	Scrapes the basketball reference schedule page for dates, games and teams playing
	"""
	def handle(self, *args, **options):
		# get the content of rotoworld's nba player page
		url = 'http://www.basketball-reference.com/leagues/NBA_2015_games.html'
		r = requests.get(url)

		bs = BeautifulSoup(r.text)
		table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="games")
		rows = table.findAll(lambda tag: tag.name=='tr')

		for row in rows:
			cells = row.findAll('td')
			i = 0
			for cell in cells:
				value = cell.text
				if i == 0:
					value = value[5:]
					date = value.replace(',','')
					date_object = datetime.strptime(date, '%b %d %Y')
				elif i == 1:
					link = str(cell.a)
					box_score_link = link[10:37]
				elif i == 2:
					link = str(cell.a)
					away_team = link[16:19]
				elif i == 3:
					if value:
						away_points = value
					else:
						away_points = 0
				elif i == 4:
					link = str(cell.a)
					home_team = link[16:19]
				elif i == 5:
					if value:
						home_points = value
					else:
						home_points = 0

				i += 1


			if row.find('td'):
				game = Game.objects.create(date=date_object, box_score_link=box_score_link,
					away_team=away_team, away_points=away_points, home_team=home_team, 
					home_points=home_points)
				print('Loaded game: {}'.format(game))
