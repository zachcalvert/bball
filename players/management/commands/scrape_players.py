import copper
import pandas as pd
import requests
from bs4 import BeautifulSoup

from players.models import Player
from players.utils import rename_players, create_players, remove_created_teams

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Scrapes the rotoworld player page to import current NBA players into the app.
    TODO: does not pull in the team they play for currently
    """
    def handle(self, *args, **options):
    	# get the content of rotoworld's nba player page
		url = 'http://www.rotoworld.com/teams/depth-charts/nba.aspx'
		r = requests.get(url)

		soup = BeautifulSoup(r.text)
		table = soup.find_all('table', class_='depthtable')

		# first player listed is a PG
		position = 'PG'

		for row in table:
			trs = row.find_all('tr')
			for tr in trs:
				if tr.b:
					position = str(tr.b).strip("<b>/")
				info = tr.a
				# create the player
				player = Player.objects.get_or_create(name=info.text, position=position)
				# sanity check
				print('created player: {0}, {1}'.format(info.text, position))


		rename_players()
		create_players()
		remove_created_teams()
