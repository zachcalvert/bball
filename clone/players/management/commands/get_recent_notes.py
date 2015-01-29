import requests
from bs4 import BeautifulSoup

from players.models import Player

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    Retrieves recent notes from the player's roto page
    """
    def handle(self, *args, **options):

		player = Player.objects.get(name='Kevin Martin')
		url = 'http://www.rotoworld.com/player/nba/{}'.format(player.roto_id)
		r = requests.get(url)
		soup = BeautifulSoup(r.text)
		news = soup.find_all('div', class_='playernews')

		for div in news:
			report = div.find_all("div", {"class":"report"})
			r = str(report).strip("""[<div class="report">""")
			r = r.strip("</div>]")

    		pre_impact = div.find_all("div", {"class":"impact"})
    		i = str(pre_impact).strip("""[<div class="impact">""")
    		split = i.split("<")
    		impact = split[0]

    		print("report: {}".format(r))
    		print("impact: {}".format(impact))