from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from datetime import datetime

from schedule.models import Matchup
from teams.models import Team
from teams.utils import calculate_totals, calculate_avgs

today = datetime.today()
season_start = datetime(2014, 10, 28)
delta = today - season_start
days_since_season_start = delta.days
date = today.date()

this_weeks_matchups = Matchup.objects.filter(start_date__lte=today, end_date__gte=today)

def all_matchups(request):
	matchups_by_date = []
	matchups = Matchup.objects.all().order_by('start_date')
	matchups = list(matchups)

	while matchups:
		this_week = matchups[:6]
		del matchups[:6]
		matchups_by_date.append(this_week)

	return render(request, "schedule/full-schedule.html", {"matchups_by_date": matchups_by_date})

def all_team_matchups(request, team_id):
	team = get_object_or_404(Team, pk=team_id)
	matchups = team.matchups.order_by('start_date')
	return render(request, "schedule/all_team_matchups.html", {"matchups": matchups})

def matchup(request, matchup_id):
	matchup = get_object_or_404(Matchup, pk=matchup_id)
	home_stats = calculate_totals(matchup.home_team, start_day=matchup.start_date, end_day=matchup.end_date)
	away_stats = calculate_totals(matchup.away_team, start_day=matchup.start_date, end_day=matchup.end_date)
	home_totals = home_stats.pop('totals')
	away_totals = away_stats.pop('totals')

	return render(request, "schedule/matchup.html", {"matchup": matchup, "home_stats": home_stats, 
		"away_stats": away_stats, "date": date, "home_totals": home_totals, "away_totals": away_totals})	

