import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from players.models import Player
from schedule.models import StatLine

from django.core.management.base import BaseCommand

stat_map = {1: "name", 2: "nba_team", 6: "minutes", 7: "fgm", 8: "fga", 10: "threes", 
			13: "ftm", 14: "fta", 18: "rebounds", 19: "assists",
        	20: "steals", 21: "blocks", 22: "turnovers", 24: "points"}

class Command(BaseCommand):
    """
    Retrieves stats from the previous day. Runs daily at 2:00am PST.
    """
    def handle(self, *args, **options):
        StatLine.objects.filter(mp=240).delete()
        StatLine.objects.filter(mp=265).delete()
        StatLine.objects.filter(mp=290).delete()
        StatLine.objects.filter(mp=315).delete()
        Player.objects.filter(name='Team Totals').delete()

    	# calculate days since start of season
    	today = datetime.today()
    	season_start = datetime(2014, 10, 28)
    	delta = today - season_start
    	days_to_calculate = delta.days

        while days_to_calculate > 0:
            print("days left: {}".format(days_to_calculate))
            the_day = today - timedelta(days=days_to_calculate)
            day = the_day.date()

            # get statlines for that day
            sls = StatLine.objects.filter(game__date=day, added_to_player=False)
            for sl in sls:
                try:
                    player = Player.objects.get(id=sl.player_id)
                except Player.DoesNotExist:
                    print("could not find player {}".format(sl.player_id))
                    continue
                player.games_played += 1
                mins = sl.mp.rsplit(':')[0]
                player.minutes += int(mins)
                player.fgm += sl.fgm
                player.fga += sl.fga
                player.ftm += sl.ftm
                player.fta += sl.fta
                player.points += sl.pts
                player.threes += sl.threesm
                player.assists += sl.asts
                player.rebounds += sl.trbs
                player.steals += sl.stls
                player.blocks += sl.blks
                player.turnovers += sl.tos
                player.save()
                sl.added_to_player = True
                sl.save()
                print("loaded stats for player {0} on {1}".format(player.name, day))

            days_to_calculate = days_to_calculate - 1
