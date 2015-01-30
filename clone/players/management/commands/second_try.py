from pygoogle import pygoogle
from time import sleep
import re
import requests
from bs4 import BeautifulSoup

from players.models import Player

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Gets the ids of players to fetch their notes. Brute forces the rotoworld urls since they are formatted with ids
    """
    def handle(self, *args, **options):
        i = 2361
        while i < 2420:
            url = 'http://www.rotoworld.com/player/nba/{}/'.format(i)
            r = requests.get(url)
            soup = BeautifulSoup(r.text)
            playername = soup.find_all('div', class_='playername')

            name = (str(playername))
            name = name[29:]
            name = name.split('|')
            name = (name[0])
            name = name[:-1]

            print("trying to find player: {}.".format(name))
            try:
                player = Player.objects.get(name=name)
                print("found")
            except Player.DoesNotExist:
                print("not found")
                i += 1
                continue

            player.roto_id = i
            player.save()
            i += 1 
