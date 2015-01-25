from players.models import Player

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Resets all player stats
    """
    def handle(self, *args, **options):
		players = Player.objects.all()
		for player in players:
			player.games_played = 0
			player.minutes = 0
			player.fgm = 0
			player.fga = 0
			player.ftm = 0
			player.fta = 0
			player.fta = 0
			player.points = 0
			player.threes = 0
			player.rebounds = 0
			player.assists = 0
			player.steals = 0
			player.blocks = 0
			player.turnovers = 0
			player.save()