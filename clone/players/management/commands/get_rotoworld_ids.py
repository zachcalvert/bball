from pygoogle import pygoogle

from players.models import Player

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Gets the ids of players to fetch their notes.
    """
    def handle(self, *args, **options):

        for player in Player.objects.all():
            g = pygoogle('rotoworld {}'.format(player.name))
            g.pages = 1
            r = g.get_urls()

            roto_url = r[0]
            roto_id = roto_url.split('/')[5];

            print("""{0}'s roto_id is {1}""".format(player.name, roto_id))
            player.roto_id = roto_id
            player.save()