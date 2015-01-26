from django.shortcuts import get_object_or_404, render
from django_tables2   import RequestConfig
from django.conf import settings
from datetime import datetime

from teams.models import Team

now = datetime.now()
date = now.date()

def home(request):
	return render(request, "teams/index.html")

def all_teams(request):
	teams = Team.objects.all()
	return render(request, "teams/all_teams.html", {'teams': teams})

def team_profile(request, team_id):
	team = Team.objects.get(id=team_id)
	return render(request, "teams/team_profile.html", {'team': team, 'date': date})

