from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.conf import settings

from players.models import Player
from datetime import datetime, timedelta, date
from players.utils import get_image_url, calculate_recent_totals, calculate_recent_avgs

today = datetime.today()
season_start = datetime(2014, 10, 28)
delta = today - season_start
days_since_season_start = delta.days

def index(request):
	return render(request, "players/index.html")

def all_averages(request):
	players = Player.objects.all()
	return render(request, "players/all/all_averages.html", {"today": today, "players": players})

def free_agents(request):
	players = Player.objects.filter(team__isnull=True)
	return render(request, "players/all/all_averages.html", {"today": today, "players": players})

def player_profile(request, player_id):
	player = get_object_or_404(Player, pk=player_id)
	url = get_image_url(player.name)
	total_stats = calculate_recent_totals(player, days_since_season_start)
	avg_stats = calculate_recent_avgs(total_stats)
	return render(request, 'players/player_profile.html', {'player': player, 'image_url': url, 'total_stats': total_stats, 'avg_stats': avg_stats})

def last_month(request, player_id):
	num_days=30
	player = Player.objects.get(id=player_id)
	url = get_image_url(player.name)
	total_stats = calculate_recent_totals(player, num_days)
	avg_stats = calculate_recent_avgs(total_stats)
	return render(request, 'players/player_profile.html', {'player':player, 'image_url': url, 'total_stats': total_stats, 'avg_stats': avg_stats})

def last_fifteen(request, player_id):
	num_days=15
	player = Player.objects.get(id=player_id)
	url = get_image_url(player.name)
	total_stats = calculate_recent_totals(player, num_days)
	avg_stats = calculate_recent_avgs(total_stats)
	return render(request, 'players/player_profile.html', {'player':player, 'image_url': url, 'total_stats': total_stats, 'avg_stats': avg_stats})

def last_week(request, player_id):
	num_days=7
	player = Player.objects.get(id=player_id)
	url = get_image_url(player.name)
	total_stats = calculate_recent_totals(player, num_days)
	avg_stats = calculate_recent_avgs(total_stats)
	return render(request, 'players/player_profile.html', {'player':player, 'image_url': url, 'total_stats': total_stats, 'avg_stats': avg_stats})


