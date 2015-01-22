import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from players.models import Player

from django.core.management.base import BaseCommand

stat_map = {1: "name", 2: "nba_team", 6: "minutes", 7: "fgm", 8: "fga", 10: "threes", 
			13: "ftm", 14: "fta", 18: "rebounds", 19: "assists",
        	20: "steals", 21: "blocks", 22: "turnovers", 24: "points"}

class Command(BaseCommand):
    """
    Retrieves stats from the previous day. Runs daily at 2:00am PST.
    """
    def handle(self, *args, **options):

    	# calculate days since start of season
    	today = datetime.today()
    	season_start = datetime(2014, 10, 28)
    	delta = today - season_start
    	days_to_calculate = delta.days

    	while days_to_calculate > 0:
    		print("days left: {}".format(days_to_calculate))
    		# construct the url to scrape
    		the_day = today - timedelta(days=days_to_calculate)
    		month = the_day.month
    		year = the_day.year
    		day = the_day.day
    		url = """http://www.basketball-reference.com/friv/dailyleaders.cgi?month={0}&day={1}&year={2}""".format(month, day, year)
    		print(url)

	    	response = requests.get(url)
	    	bs = BeautifulSoup(response.text)
	    	table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="stats")
	    	try:
	    		rows = table.findAll(lambda tag: tag.name=='tr')
	    		# if no stats for that day, skip to the next day
	    	except Exception:
	    		days_to_calculate = days_to_calculate - 1
	    		continue

	    	for row in rows:
	    		cells = row.findChildren('td')
	    		i = 0
	    		player_stats = {}
	    		for cell in cells:
	    			value = cell.string
	    			k = stat_map.get(i)
	    			if k:
	    				if k == "minutes":
	    					value = value[3:]
	    				player_stats[k] = value
		    		i += 1

		    	name = player_stats.get("name")
		    	if name is not None:
		    		player_stats.pop("name")
		    		team = player_stats.pop("nba_team")
			    	try:
			    		player = Player.objects.get(name=name)
			    	except Player.DoesNotExist:
			    		print('failed to find player: {0}'.format(name))
			    		pass

			    	# increment the players' stats
			    	for k, v in player_stats.items():
			    		stat = getattr(player, k)
			    		stat = int(v) + int(stat)
			    		player.__setattr__(k,stat)

			    	player.nba_team = team
			    	player.games += 1
			    	player.save()

		
		days_to_calculate = days_to_calculate - 1


