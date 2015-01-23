import requests
from bs4 import BeautifulSoup

from schedule.models import Game

from django.core.management.base import BaseCommand

months = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "Oct": '10', "Nov": '11', "Dec": '12'}

def format_date(date_string):
	date = date_string[5:]
	date = date.replace(',','').replace(' ','-')
	# get month
	month_as_string = date[:3]
	month = months.get(month_as_string)
	# get day
	date = date[4:]
	day = date.rsplit('-', 1)[0]
	x = int(day)
	# prepend 0 if necessary
	if x < 10:
		day = '0' + day
	# get year
	date = date.replace('-',' ')
	date.split()
	year = date[2:]
	year = year.replace(' ', '')

	retval = year + month + day



class Command(BaseCommand):
    """
    Scrapes the basketball reference schedule page for dates, games and teams playing
    """
    def handle(self, *args, **options):
    	# get the content of rotoworld's nba player page
		url = 'http://www.basketball-reference.com/leagues/NBA_2015_games.html'
		r = requests.get(url)

		soup = BeautifulSoup(r.text)
		table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="games")
    	rows = table.findAll(lambda tag: tag.name=='tr')

    	for row in rows:
    		cells = row.findChildren('td')
    		i =0
    		for cell in cells:
    			value = cell.string
    			
    			# date
    			if i == 0:





