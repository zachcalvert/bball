from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from datetime import datetime

from schedule.models import Matchup
from teams.models import Team
from teams.utils import calculate_team_totals, calculate_team_avgs

today = datetime.today()
season_start = datetime(2014, 10, 28)
delta = today - season_start
days_since_start = delta.days
date = today.date()

context_data = {}
context_data['days_since_start'] = days_since_start

this_weeks_matchups = Matchup.objects.filter(start_date__lte=today, end_date__gte=today)

@login_required(login_url='login')
def all_matchups(request):
	context_data['user_team'] = Team.objects.get(owner=request.user.id)

	matchups_by_date = []
	matchups = Matchup.objects.all().order_by('start_date')
	matchups = list(matchups)

	while matchups:
		this_week = matchups[:6]
		del matchups[:6]
		matchups_by_date.append(this_week)

	context_data['matchups_by_date'] = matchups_by_date

	return render(request, "schedule/full-schedule.html", context_data)

@login_required(login_url='login')
def all_team_matchups(request, team_id):
	context_data['user_team'] = Team.objects.get(owner=request.user.id)

	team = get_object_or_404(Team, pk=team_id)
	matchups = team.matchups.order_by('start_date')
	context_data['matchups'] = matchups

	return render(request, "schedule/all_team_matchups.html", context_data)

@login_required(login_url='login')
def matchup(request, matchup_id):
	context_data['user_team'] = Team.objects.get(owner=request.user.id)

	matchup = get_object_or_404(Matchup, pk=matchup_id)
	context_data['matchup'] = matchup

	home_stats = calculate_team_totals(matchup.home_team, start_day=matchup.start_date, end_day=matchup.end_date)
	away_stats = calculate_team_totals(matchup.away_team, start_day=matchup.start_date, end_day=matchup.end_date)
	context_data['home_stats'] = home_stats
	context_data['away_stats'] = away_stats

	home_totals = home_stats.pop('totals')
	away_totals = away_stats.pop('totals')
	context_data['home_totals'] = home_totals
	context_data['away_totals'] = away_totals

	return render(request, "schedule/matchup.html", context_data)	

@login_required(login_url='login')
def standings(request):
	context_data['user_team'] = Team.objects.get(owner=request.user.id)
	
	teams = Team.objects.all()
	context_data['teams'] = teams
	return render(request, "schedule/standings.html", context_data)

