from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.views.decorators.cache import cache_page

from players.models import Player
from teams.models import Team
from datetime import datetime, timedelta, date
from players.utils import get_image_url, calculate_totals, calculate_avgs
from teams.utils import calculate_team_totals, calculate_team_avgs

today = datetime.today()
season_start = datetime(2014, 10, 28)
thirty = timedelta(days=30)
fifteen = timedelta(days=15)
seven = timedelta(days=7)
days_since_start = (today-season_start).days

def index(request):
	return render(request, "players/index.html")

def all_averages(request):
	players = Player.objects.all()
	return render(request, "players/all/all_averages.html", {"today": today, "players": players})

@cache_page(60*30)
def free_agents(request, num_days=days_since_start):
	delta = timedelta(days=int(num_days))
	start_day = today - delta
	all_player_stats = {}
	players = Player.objects.filter(team__isnull=True)[:150]
	for player in players:
		all_player_stats[player.id] = {}
		total_stats = calculate_totals(player, start_day=start_day, end_day=today)
		avg_stats = calculate_avgs(total_stats)
		all_player_stats[player.id]['name'] = player.name
		all_player_stats[player.id]['nba_team'] = player.nba_team
		all_player_stats[player.id]['position'] = player.position
		all_player_stats[player.id]['stats'] = avg_stats
	return render(request, "players/all/all_averages.html", {"days_since_start": days_since_start, "num_days": num_days, "all_player_stats": all_player_stats})

def add_player(request, player_id, num_days=days_since_start):
	player = get_object_or_404(Player, pk=player_id)
	delta = timedelta(days=int(num_days))
	start_day = today - delta
	player_stats = calculate_totals(player, start_day=start_day, end_day=today)
	player_avg_stats = calculate_avgs(player_stats)

	team = Team.objects.first()
	team_total_stats = calculate_team_totals(team, start_day=start_day, end_day=today)
	team_avg_stats = calculate_team_avgs(team_total_stats)
	team_avg_stats.pop('totals')

	return render(request, "players/add_player.html", {"days_since_start": days_since_start, "num_days": num_days, 
		"player_avg_stats": player_avg_stats, "team_avg_stats": team_avg_stats})



def player_profile(request, player_id):
	player = get_object_or_404(Player, pk=player_id)
	url = get_image_url(player.name)
	total_stats = calculate_totals(player, start_day=season_start, end_day=today)
	avg_stats = calculate_avgs(total_stats)
	return render(request, 'players/player_profile.html', {'player': player, 'image_url': url, 'total_stats': total_stats, 'avg_stats': avg_stats})



