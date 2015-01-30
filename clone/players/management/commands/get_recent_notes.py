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

        player_notes = ''
        t = 0
        for div in news:
            if t > 1500:
                continue
            else:
                report = div.find_all("div", {"class":"report"})
                r = str(report).strip("""[<div class="report">""")
                r = r.strip("</div>]") 

                pre_impact = div.find_all("div", {"class":"impact"})
                i = str(pre_impact).strip("""[<div class="impact">""")
                split = i.split("<")
                impact = split[0] 
                pre_date = split[1].split(">")
                date = pre_date[1].split("-")
                date = date[0]

                d = "date: {}\n".format(date)
                r = "report: {}\n".format(r)
                i = "impact: {}\n".format(impact)

                player_notes += d
                player_notes += r 
                player_notes += i 
                player_notes+= '\n'
                t = len(player_notes)

        print(len(player_notes))
        print(player_notes)