from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django_tables2   import RequestConfig
from django.conf import settings

from players.models import Player, PlayerTable
from datetime import datetime, timedelta, date
from players.utils import get_image_url

now = datetime.now()
today = now.date()

def index(request):
	return render(request, "teams/index.html")

def all_totals(request):
	table = PlayerTable(Player.objects.all())
	RequestConfig(request, paginate=False).configure(table)
	return render(request, "players/all/totals.html", {"table": table})

def all_averages(request):
	players = Player.objects.all()
	return render(request, "players/all/averages.html", {"players": players})

def player_profile(request, player_id):
	player = get_object_or_404(Player, pk=player_id)
	url = get_image_url(player.name)
	now = datetime.now()
	date = now.date()
	return render(request, 'players/player_profile.html', {'player': player, 'image_url': url, 'date': date})

def get_recent_stats(request, player_id, days):
	delta = timedelta(days=days)
	start_day = today - delta
	statlines = StatLine.objects.filter(player_id=player_id, game__date__gte=start_day)
	stats = stringify_stats(statlines)
	return render(request, 'players/last_fifteen/averages.html', stats) 
