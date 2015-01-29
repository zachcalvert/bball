from django.shortcuts import get_object_or_404, render
from django_tables2   import RequestConfig
from django.conf import settings
from datetime import datetime

from teams.models import Team
from teams.utils import calculate_recent_totals, calculate_recent_avgs

today = datetime.today()
season_start = datetime(2014, 10, 28)
delta = today - season_start
days_since_season_start = delta.days
date = today.date()


def home(request):
	return render(request, "teams/site_base.html")

def all_teams(request):
	teams = Team.objects.all()
	return render(request, "teams/all_teams.html", {'teams': teams})

def team_profile(request, team_id):
	team = Team.objects.get(id=team_id)
	total_stats = calculate_recent_totals(team, days_since_season_start)
	avg_stats = calculate_recent_avgs(total_stats)
	return render(request, "teams/team_profile.html", {'team': team, 'total_stats': total_stats, 'avg_stats': avg_stats, 'date': date})

def team_last_month(request, team_id):
	num_days=30
	team = Team.objects.get(id=team_id)
	total_stats = calculate_recent_totals(team, num_days)
	avg_stats = calculate_recent_avgs(total_stats)
	return render(request, 'teams/team_profile.html', {'team':team, 'total_stats': total_stats, 'avg_stats': avg_stats, 'date': date})

def team_last_fifteen(request, team_id):
	num_days=15
	team = Team.objects.get(id=team_id)
	total_stats = calculate_recent_totals(team, num_days)
	avg_stats = calculate_recent_avgs(total_stats)
	return render(request, 'teams/team_profile.html', {'team':team, 'total_stats': total_stats, 'avg_stats': avg_stats, 'date': date})

def team_last_week(request, team_id):
	num_days=7
	team = Team.objects.get(id=team_id)
	total_stats = calculate_recent_totals(team, num_days)
	avg_stats = calculate_recent_avgs(total_stats)
	return render(request, 'teams/team_profile.html', {'team':team, 'total_stats': total_stats, 'avg_stats': avg_stats, 'date': date})
	
