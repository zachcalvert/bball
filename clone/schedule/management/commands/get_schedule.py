import requests
from bs4 import BeautifulSoup

from schedule.models import Game
from schedule.utils import format_date

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
			print(len(cells))
			i =0
			for cell in cells:
				print("string {}".format(cell.string))
				value = cell.string

    			# date
    			if i == 0:
    				if value:
    					date = format_date(value)
    			elif i == 1:
    				if value:
    					box_score_link = value
    			elif i == 2:
    				if value:
    					away_team = value
    			elif i == 3:
    				if value:
    					away_points = value
    			elif i == 4:
    				if value:
    					home_team = value
    			elif i == 5:
    				if value:
    					home_points = value

    			print("date: {}".format(date))
    			i += 1






