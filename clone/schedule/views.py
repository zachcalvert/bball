from django.shortcuts import render, get_object_or_404
from schedule.models import Matchup

# Create your views here.

today = datetime.today()
this_weeks_matchups = Matchup.objects.filter(start_date__lte=today, end_date__gte=today)

def current_matcup(request, team_id):
	team = get_object_or_404(Team, pk=team_id)
	matchup = this_weeks_matchups.filter(Q(home_team=team) | Q(away_team=team))

