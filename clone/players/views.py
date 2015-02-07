from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings

from players.models import Player
from datetime import datetime, timedelta, date
from players.utils import get_image_url, calculate_totals, calculate_avgs

today = datetime.today()
season_start = datetime(2014, 10, 28)
thirty = timedelta(days=30)
fifteen = timedelta(days=15)
seven = timedelta(days=7)

def index(request):
	return render(request, "players/index.html")

def all_averages(request):
	players = Player.objects.all()
	return render(request, "players/all/all_averages.html", {"today": today, "players": players})

def free_agents(request):
	all_player_stats = {}
	players = Player.objects.filter(team__isnull=True)[:50]
	for player in players:
		all_player_stats[player.id] = {}
		total_stats = calculate_totals(player, start_day=season_start, end_day=today)
		avg_stats = calculate_avgs(total_stats)
		all_player_stats[player.id]['name'] = player.name
		all_player_stats[player.id]['nba_team'] = player.nba_team
		all_player_stats[player.id]['position'] = player.position
		all_player_stats[player.id]['stats'] = avg_stats
	return render(request, "players/all/all_averages.html", {"today": today, "all_player_stats": all_player_stats})

def player_profile(request, player_id):
	player = get_object_or_404(Player, pk=player_id)
	url = get_image_url(player.name)
	total_stats = calculate_totals(player, start_day=season_start, end_day=today)
	avg_stats = calculate_avgs(total_stats)
	return render(request, 'players/player_profile.html', {'player': player, 'image_url': url, 'total_stats': total_stats, 'avg_stats': avg_stats})

def last_month(request, player_id):
	player = Player.objects.get(id=player_id)
	url = get_image_url(player.name)
	start_day = today - thirty
	total_stats = calculate_totals(player, start_day=start_day, end_day=today)
	avg_stats = calculate_avgs(total_stats)
	return render(request, 'players/player_profile.html', {'player':player, 'image_url': url, 'total_stats': total_stats, 'avg_stats': avg_stats})

def last_fifteen(request, player_id):
	player = Player.objects.get(id=player_id)
	url = get_image_url(player.name)
	start_day = today - fifteen
	total_stats = calculate_totals(player, start_day=start_day, end_day=today)
	avg_stats = calculate_avgs(total_stats)
	return render(request, 'players/player_profile.html', {'player':player, 'image_url': url, 'total_stats': total_stats, 'avg_stats': avg_stats})

def last_week(request, player_id):
	player = Player.objects.get(id=player_id)
	url = get_image_url(player.name)
	start_day = today - seven
	total_stats = calculate_totals(player, start_day=start_day, end_day=today)
	avg_stats = calculate_avgs(total_stats)
	return render(request, 'players/player_profile.html', {'player':player, 'image_url': url, 'total_stats': total_stats, 'avg_stats': avg_stats})


