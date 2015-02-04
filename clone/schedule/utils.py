from datetime import date
from schedule.models import Matchup, StatLine
from django.db.models import Q

months = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "Oct": '10', "Nov": '11', "Dec": '12'}

def format_date_for_box_score(date_string):
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

	return year + month + day