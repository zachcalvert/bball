from datetime import datetime, timedelta, date

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
