from datetime import datetime, timedelta, date
from dateutil import rrule

from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from schedule.models import Matchup
from teams.models import Team
from teams.utils import calculate_team_totals, calculate_team_avgs

context_data = {}

today = datetime.today()
this_weeks_matchups = Matchup.objects.filter(start_date__lte=today, end_date__gte=today)

@login_required(login_url='login')
def all_matchups(request):
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
	team = get_object_or_404(Team, pk=team_id)
	matchups = team.matchups.order_by('start_date')
	context_data['matchups'] = matchups

	return render(request, "schedule/all_team_matchups.html", context_data)


@login_required(login_url='login')
def matchup(request, matchup_id):
	matchup = get_object_or_404(Matchup, pk=matchup_id)
	context_data['matchup'] = matchup

	home_stats = calculate_team_totals(matchup.home_team, start_day=matchup.start_date, end_day=matchup.end_date)
	away_stats = calculate_team_totals(matchup.away_team, start_day=matchup.start_date, end_day=matchup.end_date)
	home_totals = home_stats.pop('totals')
	away_totals = away_stats.pop('totals')
	context_data['home_totals'] = home_totals
	context_data['away_totals'] = away_totals

	# attach matchup games for each player
	for player in matchup.home_team.players:
		home_stats[player.id]['matchup_games'] = player.matchup_games(matchup)
	for player in matchup.away_team.players:
		away_stats[player.id]['matchup_games'] = player.matchup_games(matchup)

	context_data['home_stats'] = home_stats
	context_data['away_stats'] = away_stats

	return render(request, "matchup.html", context_data)	


@login_required(login_url='login')
def standings(request):
	teams = Team.objects.all()
	context_data['teams'] = teams
	return render(request, "season_standings.html", context_data)



def current_week():
	season_start = datetime(2014, 10, 27)
	season_end = datetime(2015, 4, 15)

	z = 1
	for dt in rrule.rrule(rrule.WEEKLY, dtstart=season_start, until=season_end):
		one_week = timedelta(days=6)
		end_date = dt + one_week
		if dt <= today <= end_date:
			return z
		elif z < 23:
			z += 1
			continue
		else:
			return 23

@login_required(login_url='login')
def scoreboard(request, week_id=1):
	matchups = Matchup.objects.filter(week=current_week())
	context_data['matchups'] = matchups
	return render_to_response("scoreboard.html", context_data,
		context_instance=RequestContext(request))

