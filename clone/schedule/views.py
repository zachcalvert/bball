from django.shortcuts import render, get_object_or_404
from schedule.models import Matchup
from teams.models import Team

from datetime import datetime

# Create your views here.

today = datetime.today()
this_weeks_matchups = Matchup.objects.filter(start_date__lte=today, end_date__gte=today)

def all_matchups(request):
	matchups_by_date = []
	matchups = Matchup.objects.all().order_by('start_date')
	matchups = list(matchups)

	while matchups:
		this_week = matchups[:6]
		del matchups[:6]
		matchups_by_date.append(this_week)

	print(matchups_by_date)
	return render(request, "schedule/full-schedule.html", {"matchups_by_date": matchups_by_date})

def current_matchup(request, team_id):
	team = get_object_or_404(Team, pk=team_id)
	matchup = this_weeks_matchups.filter(Q(home_team=team) | Q(away_team=team))
	return render(request, "schedule/current_matchup.html", {"matchup": matchup})

def all_team_matchups(request, team_id):
	team = get_object_or_404(Team, pk=team_id)
	matchups = team.matchups.order_by('start_date')
	return render(request, "schedule/all_team_matchups.html", {"matchups": matchups})	
		

