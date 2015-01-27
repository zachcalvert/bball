from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django_tables2   import RequestConfig
from django.conf import settings

from players.models import Player, PlayerTable
from datetime import datetime, timedelta, date
from players.utils import get_image_url, calculate_average_stats

today = datetime.today()
season_start = datetime(2014, 10, 28)
delta = today - season_start
days_since_season_start = delta.days

def index(request):
	return render(request, "teams/index.html")

def all_totals(request):
	table = PlayerTable(Player.objects.all())
	RequestConfig(request, paginate=False).configure(table)
	return render(request, "players/all/all_totals.html", {"table": table})

def all_averages(request):
	players = Player.objects.all()
	return render(request, "players/all/averages.html", {"players": players})

def player_profile(request, player_id):
	player = get_object_or_404(Player, pk=player_id)
	url = get_image_url(player.name)
	stats = calculate_average_stats(player, days_since_season_start)
	return render(request, 'players/player_profile.html', {'player': player, 'image_url': url, 'stats': stats})

def last_month(request, player_id):
	num_days=30
	player = Player.objects.get(id=player_id)
	url = get_image_url(player.name)
	stats = calculate_average_stats(player, num_days)
	return render(request, 'players/player_profile.html', {'player':player, 'image_url': url, 'stats': stats})

def last_fifteen(request, player_id):
	num_days=15
	player = Player.objects.get(id=player_id)
	url = get_image_url(player.name)
	stats = calculate_average_stats(player, num_days)
	return render(request, 'players/player_profile.html', {'player':player, 'image_url': url, 'stats': stats})

def last_week(request, player_id):
	num_days=7
	player = Player.objects.get(id=player_id)
	url = get_image_url(player.name)
	stats = calculate_average_stats(player, num_days)
	return render(request, 'players/player_profile.html', {'player':player, 'image_url': url, 'stats': stats})


