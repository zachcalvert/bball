import copper
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from players.models import Player
from players.utils import get_yesterdays_url

from django.core.management.base import BaseCommand

stat_map = {1: "name", 2: "nba_team", 7: "fgm", 8: "fga", 10: "threes", 
			13: "ftm", 14: "fta", 18: "rebounds", 19: "assists",
        	20: "steals", 21: "blocks", 22: "turnovers", 24: "points"}

class Command(BaseCommand):
    """
    Retrieves stats from the previous day. Runs daily at 2:00am PST.
    """
    def handle(self, *args, **options):
    	url = get_yesterdays_url()
    	print(url)
    	response = requests.get(url)
    	bs = BeautifulSoup(response.text)
    	table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="stats")
    	rows = table.findAll(lambda tag: tag.name=='tr')

    	for row in rows:
    		cells = row.findChildren('td')
    		i = 0
    		player_stats = {}
    		for cell in cells:
    			value = cell.string
    			k = stat_map.get(i)
    			if k:
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

		    	# increment the players' stats
		    	for k, v in player_stats.items():
		    		stat = getattr(player, k)
		    		stat = int(v) + int(stat)
		    		player.__setattr__(k,stat)

		    	player.nba_team = team
		    	player.save()
		    	print('saved player: {} \n'.format(player.name))