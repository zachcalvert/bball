from __future__ import division
from datetime import datetime, timedelta
from players.models import Player
from schedule.models import Game, StatLine
from django.db.models import Q

ROOT_IMAGE_URL = """http://i.cdn.turner.com/nba/nba/.element/img/2.0/sect/statscube/players/large/"""

def get_image_url(player_name):
	name = player_name.replace(' ','_').lower()
	return "{0}{1}.png".format(ROOT_IMAGE_URL,name)


def todays_opponent(player_id):
	player = Player.objects.get(id=player_id)
	now = datetime.now()
	games = Game.objects.filter(Q(home_team=player.nba_team)| Q(away_team=player.nba_team))
	for game in games:
		if game.date == now.date():
			if game.away_team == player.nba_team:
				return '@{}'.format(game.home_team)
			elif game.home_team == player.nba_team:
				return game.away_team

def todays_game_status(player_id):
	player = Player.objects.get(id=player_id)
	now = datetime.now()
	games = Game.objects.filter(Q(home_team=player.nba_team)| Q(away_team=player.nba_team))
	for game in games:
		if game.date == now.date():
			return game.tipoff


def calculate_average_stats(player, num_days):

	now = datetime.now()
	today = now.day
	then = now - timedelta(days=num_days)
	that_day = then.date()

	games_played = 0
	stats = {"minutes": 0, "fgm": 0, "fga": 0, "ftm": 0, "fta": 0, "threes": 0, "rebounds": 0, "assists": 0, "steals": 0, "blocks": 0, "turnovers": 0, "points": 0} 

	games = Game.objects.filter(Q(home_team=player.nba_team)| Q(away_team=player.nba_team))
	games = games.filter(date__gte=that_day)

	for game in games:
		try:
			sl = StatLine.objects.get(game_id=game.id, player_id=player.id)
		except StatLine.DoesNotExist:
			continue
		if sl:
			games_played += 1
			stats['minutes'] += int(sl.mp[:2])
			stats['fgm'] += int(sl.fgm)
			stats['fga'] += int(sl.fga)
			stats['ftm'] += int(sl.ftm)
			stats['fta'] += int(sl.fta)
			stats['threes'] += int(sl.threesm)
			stats['rebounds'] += int(sl.trbs)
			stats['assists'] += int(sl.asts)
			stats['steals'] += int(sl.stls)
			stats['blocks'] += int(sl.blks)
			stats['turnovers'] += int(sl.tos)
			stats['points'] += int(sl.pts)

	for k, v in stats.items():
		avg = v/games_played
		stats[k] = round(avg, 1)

	return stats


def remove_created_teams():
	non_players = ('Atlanta Hawks', 'Charlotte Hornets', 'Dallas Mavericks', 'Golden State Warriors',
		'Los Angeles Clippers', 'Miami Heat', 'New Orleans Pelicans', 'Orlando Magic',
		'Portland Trail Blazers', 'Toronto Raptors',) 
	for non_player in non_players:
		player = Player.objects.get(name=non_player)
		player.delete()

def create_players():
	players = {"Austin Daye": "SF","""A.J. Price""": "PG","""Alex Kirk""": "C","""Brandon Davies""": "PF",
	"""Chris Douglas-Roberts""":"SF","""Chris Johnson""":"C","""Francisco Garcia""":"SF","""Glen Rice""":"SG",
	"""Jeff Adrien""":"C","""Jeffery Taylor""":"SF","""Jordan Farmar""":"PG","""Nate Robinson""":"PG",
	"""Samuel Dalembert""":"C","""Sebastian Telfair""":"PG","""Shannon Brown""":"SG","Xavier Henry":"SF",}

	for k, v in players.items():
		player = Player.objects.get_or_create(name=k, position=v)

def rename_players():
		player = Player.objects.get(name='Lou Williams')
		player.name='Louis Williams'
		player.save()
		player = Player.objects.get(name='Amare Stoudemire')
		player.name="""Amar'e Stoudemire"""
		player.save()
		player = Player.objects.get(name='Moe Harkless')
		player.name='Maurice Harkless'
		player.save()
		player = Player.objects.get(name='J.J. Barea')
		player.name='Jose Barea'
		player.save()
		player = Player.objects.get(name='Wes Johnson')
		player.name='Wesley Johnson'
		player.nba_team = 'LAL'
		player.save()
		player = Player.objects.get(name='Tim Hardaway Jr.')
		player.name='Tim Hardaway'
		player.save()
		player = Player.objects.get(name='Ishmael Smith')
		player.name='Ish Smith'
		player.save()
		player = Player.objects.get(name='Glenn Robinson III')
		player.name='Glenn Robinson'
		player.save()
		player = Player.objects.get(name='Patty Mills')
		player.name='Patrick Mills'
		player.save()

