import requests
from bs4 import BeautifulSoup

from players.models import Player

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Gets the ids of players to fetch their notes.
    """
    def handle(self, *args, **options):
        i = 1310
        while i < 
    	# get the content of rotoworld's nba player page
		url = 'http://www.rotoworld.com/teams/depth-charts/nba.aspx'
		r = requests.get(url)

		soup = BeautifulSoup(r.text)
		table = soup.find_all('table', class_='depthtable')