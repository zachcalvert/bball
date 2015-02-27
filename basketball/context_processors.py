from datetime import datetime, timedelta, date
from dateutil import rrule

from teams.models import Team

today = datetime.today()

def days_since_start(request):
	season_start = datetime(2014, 10, 28)
	days_since_start = (today-season_start).days
	return { 'days_since_start': days_since_start }

def teams(request):
	teams = Team.objects.all()
	return { 'teams': teams }

def user_team(request):
	try:
		team = Team.objects.get(owner=request.user.id)
		return { 'user_team': team }
	except Team.DoesNotExist:
		return {'user_team': None }

def current_week(request):
	season_start = datetime(2014, 10, 27)
	season_end = datetime(2015, 4, 15)
	current_week = 1
	for dt in rrule.rrule(rrule.WEEKLY, dtstart=season_start, until=season_end):
		one_week = timedelta(days=6)
		end_date = dt + one_week
		if dt <= today <= end_date:
			return { 'current_week' : current_week }
		elif current_week < 23:
			current_week += 1
			continue
		else:
			return { 'current_week' : current_week }