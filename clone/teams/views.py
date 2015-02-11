from django.shortcuts import get_object_or_404, render
from django.conf import settings
from datetime import datetime, timedelta

from teams.models import Team
from teams.utils import calculate_team_totals, calculate_team_avgs

context_data = {}

today = datetime.today()
season_start = datetime(2014, 10, 28)
thirty = timedelta(days=30)
fifteen = timedelta(days=15)
seven = timedelta(days=7)
today_day = today.date()
days_since_start = (today-season_start).days

context_data['days_since_start'] = days_since_start

template_name = "teams/team_profile.html"

def home(request):
	if request.user.is_authenticated():
		user_team = Team.objects.get(owner=request.user.id)
	else:
		user_team = Team.objects.first()
	context_data['user_team'] = user_team
	context_data['num_days'] = days_since_start
	return render(request, "teams/site_base.html", context_data)

def all_teams(request):
	teams = Team.objects.all()
	context_data['teams'] = teams
	return render(request, "teams/all_teams.html", context_data)

def team_profile(request, team_id, num_days=days_since_start):
	team = Team.objects.get(id=team_id)
	context_data['team'] = team

	delta = timedelta(days=int(num_days))
	start_day = today - delta
	context_data['num_days'] = num_days

	total_stats = calculate_team_totals(team, start_day=start_day, end_day=today)
	stats = calculate_team_avgs(total_stats)
	stats.pop('totals')
	context_data['stats'] = stats

	return render(request, template_name, context_data)
