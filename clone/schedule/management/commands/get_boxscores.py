import requests
from bs4 import BeautifulSoup
from pprint import pprint
from datetime import date

from schedule.models import Game, StatLine
from players.models import Player

from django.core.management.base import BaseCommand

ROOT_URL = 'http://www.basketball-reference.com/'

class Command(BaseCommand):
	"""
	Scrapes the box scores on basketball reference and loads the relevant stats 
	for use in the app
	"""
	def handle(self, *args, **options):
		# can't get the boxscore for a game that hasn't been played
		games = Game.objects.all()

		for game in games:
			if date.today() <= game.date:
				continue
			else:
				url = "{0}{1}".format(ROOT_URL, game.boxscore_link)
				r = requests.get(url)
				bs = BeautifulSoup(r.text)
				away_table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="{}_basic".format(game.away_team))
				away_rows = away_table.findAll(lambda tag: tag.name=='tr')

				for row in away_rows:
					cells = row.findAll('td')
					i = 0
					for cell in cells:
						if i == 0:
							player_name = cell.text
							try:
								player = Player.objects.get(name=player_name)
							except Player.DoesNotExist:
								print("could not find player: {}".format(player_name))
								continue
							if player.nba_team == 'FA':
								player.nba_team = game.away_team
								player.save()
								print("added {0} to {1} roster".format(player.name, game.away_team))
						elif i == 1:
							mp = cell.text
						elif i == 2:
							fgm = cell.text
						elif i == 3:
							fga = cell.text
						elif i ==4:
							pass
						elif i == 5:
							threesm = cell.text
						elif i == 6:
							threesa = cell.text
						elif i ==7:
							pass
						elif i == 8:
							ftm = cell.text
						elif i == 9:
							fta = cell.text
						elif i == 10:
							pass
						elif i == 11:
							orbs = cell.text
						elif i == 12:
							drbs = cell.text
						elif i == 13:
							trbs = cell.text
						elif i == 14:
							asts = cell.text
						elif i == 15:
							stls = cell.text
						elif i == 16:
							blks = cell.text
						elif i == 17:
							tos = cell.text
						elif i == 18:
							pfs = cell.text
						elif i == 19:
							pts = cell.text

						i += 1


					if row.find('td'):
						if mp == 'Did Not Play' or mp == 'Player Suspended':
								continue
						else:
							away_statline = StatLine.objects.create(game=game, player=player,
								mp=mp, fgm=fgm, fga=fga,ftm=ftm, fta=fta, threesm=threesm, threesa=threesa,
								orbs=orbs, drbs=drbs, trbs=trbs, asts=asts, stls=stls, blks=blks, tos=tos,
								pfs=pfs,pts=pts)
							print('Loaded statline for {0} in game {1}'.format(player.name, game))

				home_table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="{}_basic".format(game.home_team))
				home_rows = home_table.findAll(lambda tag: tag.name=='tr')

				for row in home_rows:
					cells = row.findAll('td')
					i = 0
					for cell in cells:
						if i == 0:
							player_name = cell.text
							try:
								player = Player.objects.get(name=player_name)
							except Player.DoesNotExist:
								print("could not find player: {}".format(player_name))
						elif i == 1:
							mp = cell.text
						elif i == 2:
							fgm = cell.text
						elif i == 3:
							fga = cell.text
						elif i ==4:
							pass
						elif i == 5:
							threesm = cell.text
						elif i == 6:
							threesa = cell.text
						elif i ==7:
							pass
						elif i == 8:
							ftm = cell.text
						elif i == 9:
							fta = cell.text
						elif i == 10:
							pass
						elif i == 11:
							orbs = cell.text
						elif i == 12:
							drbs = cell.text
						elif i == 13:
							trbs = cell.text
						elif i == 14:
							asts = cell.text
						elif i == 15:
							stls = cell.text
						elif i == 16:
							blks = cell.text
						elif i == 17:
							tos = cell.text
						elif i == 18:
							pfs = cell.text
						elif i == 19:
							pts = cell.text

						i += 1


					if row.find('td'):
						if mp == 'Did Not Play' or mp == 'Player Suspended' or mp == 240 or mp == 265:
								continue
						else:
							home_statline = StatLine.objects.create(game_id=game.id, player_id=player.id,
								mp=mp, fgm=fgm, fga=fga,ftm=ftm, fta=fta, threesm=threesm, threesa=threesa,
								orbs=orbs, drbs=drbs, trbs=trbs, asts=asts, stls=stls, blks=blks, tos=tos,
								pfs=pfs,pts=pts)
							print('Loaded box score for {0} in game {1}'.format(player.name, game))




