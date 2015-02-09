from django.shortcuts import get_object_or_404, render
from django.conf import settings
from datetime import datetime, timedelta

from teams.models import Team
from teams.utils import calculate_totals, calculate_avgs

today = datetime.today()
season_start = datetime(2014, 10, 28)
thirty = timedelta(days=30)
fifteen = timedelta(days=15)
seven = timedelta(days=7)
today_day = today.date()
days_since_start = (today-season_start).days

template_name = "teams/team_profile.html"

def home(request):
	return render(request, "teams/site_base.html", {"days_since_start": days_since_start})

def all_teams(request):
	teams = Team.objects.all()
	return render(request, "teams/all_teams.html", {'days_since_start': days_since_start, 'teams': teams})

def team_profile(request, team_id, num_days=days_since_start):
	team = Team.objects.get(id=team_id)
	delta = timedelta(days=int(num_days))
	start_day = today - delta
	total_stats = calculate_totals(team, start_day=start_day, end_day=today)
	stats = calculate_avgs(total_stats)
	stats.pop('totals')
	return render(request, template_name, {'team': team, 'stats': stats, 'days_since_start': days_since_start, "num_days": num_days})
