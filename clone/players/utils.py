from datetime import datetime, timedelta
from players.models import Player

def get_yesterdays_url():
	now = datetime.now()
	month = now.month
	yesterday = now - timedelta(days=1)
	day = yesterday.day
	year = now.year
	url = """http://www.basketball-reference.com/friv/dailyleaders.cgi?month={0}&day={1}&year={2}""".format(month, day, year)
	return url


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

