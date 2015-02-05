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


def home(request):
	return render(request, "teams/site_base.html")

def all_teams(request):
	teams = Team.objects.all()
	return render(request, "teams/all_teams.html", {'teams': teams})

def team_profile(request, team_id):
	team = Team.objects.get(id=team_id)
	total_stats = calculate_totals(team, start_day=season_start, end_day=today)
	stats = calculate_avgs(total_stats)

	print("stats: {}".format(stats))
	return render(request, "teams/team_profile.html", {'team': team, 'total_stats': total_stats, 'stats': stats, 
		'date': today_day})

def team_last_month(request, team_id):
	team = Team.objects.get(id=team_id)
	start_day = today - thirty
	total_stats = calculate_totals(team, start_day=start_day, end_day=today)
	stats = calculate_avgs(total_stats)
	return render(request, 'teams/team_profile.html', {'team':team, 'total_stats': total_stats, 'stats': stats, 
		'date': today_day})

def team_last_fifteen(request, team_id):
	team = Team.objects.get(id=team_id)
	start_day = today - fifteen
	total_stats = calculate_totals(team, start_day=start_day, end_day=today)
	stats = calculate_avgs(total_stats)
	return render(request, 'teams/team_profile.html', {'team':team, 'total_stats': total_stats, 'stats': stats, 
		'date': today_day})

def team_last_week(request, team_id):
	team = Team.objects.get(id=team_id)
	start_day = today - seven
	total_stats = calculate_totals(team, start_day=start_day, end_day=today)
	stats = calculate_avgs(total_stats)
	return render(request, 'teams/team_profile.html', {'team':team, 'total_stats': total_stats, 'stats': stats, 
		'date': today_day})
	
