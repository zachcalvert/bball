from __future__ import division

from players.models import Player

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    recalculates season averages from the previous day. Runs daily at 2:00am PST.
    """
    def handle(self, *args, **options):
        for player in Player.objects.all():
            print("updating {}".format(player.name))
            if player.games_played != 0:
                avg_minutes = player.minutes / player.games_played
                player.mpg = round(avg_minutes, 1)

                avg_fgm = player.fgm / player.games_played
                player.fgmpg = round(avg_fgm, 1)

                avg_fga = player.fga / player.games_played
                player.fgapg = round(avg_fga, 1)

                avg_ftm = player.ftm / player.games_played
                player.ftmpg = round(avg_ftm, 1)

                avg_fta = player.fta / player.games_played
                player.ftapg = round(avg_fta, 1)

                avg_threes = player.threes / player.games_played
                player.threespg = round(avg_threes, 1)

                avg_rebounds = player.rebounds / player.games_played
                player.rpg = round(avg_rebounds, 1)

                avg_assists = player.assists / player.games_played
                player.apg = round(avg_assists, 1)

                avg_steals = player.steals / player.games_played
                player.spg = round(avg_steals, 1)

                avg_blocks = player.blocks / player.games_played
                player.bpg = round(avg_blocks, 1)

                avg_turnovers = player.turnovers / player.games_played
                player.topg = round(avg_turnovers, 1)

                avg_points = player.points / player.games_played
                player.ppg = round(avg_points, 1)

                if player.fga != 0:
                    player.fgpct = round((player.fgm / player.fga), 3)
                
                if player.fta != 0:
                    player.ftpct = round((player.ftm / player.fta), 3)

                player.save()
                print("updated {}".format(player.name))



