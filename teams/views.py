from datetime import datetime, timedelta

from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings

from teams.models import Team
from teams.utils import calculate_team_totals, calculate_team_avgs

context_data = {}
today = datetime.today()

def logout(request, template_name='registration/logged_out.html'):
	"""
	Logs the user out and displays the login form
	"""
	logout(request)
	return redirect('site_base.html')


def home(request):
	if request.user.is_authenticated():
		return render_to_response('site_base.html', 
			context_instance=RequestContext(request))
	else:
		return render_to_response('registration/login.html',
			context_instance=RequestContext(request))


@login_required(login_url='site_home')
def team_profile(request, team_id, num_days=10):
	team = Team.objects.get(id=team_id)
	context_data['team'] = team

	delta = timedelta(days=int(num_days))
	start_day = today - delta
	context_data['num_days'] = num_days

	total_stats = calculate_team_totals(team, start_day=start_day, end_day=today)
	stats = calculate_team_avgs(total_stats)
	stats.pop('totals')
	context_data['stats'] = stats

	context_data['user_team'] = Team.objects.get(owner=request.user.id)

	return render_to_response("team_profile.html", context_data, 
		context_instance=RequestContext(request))
	