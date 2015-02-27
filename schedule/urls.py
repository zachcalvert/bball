from django.conf.urls import patterns, url
from teams import urls
from schedule import views

urlpatterns = patterns('',
	url(r'^$', views.all_matchups, name='all_matchups'),
    url(r'^matchups/(?P<team_id>\d+)/$', views.all_team_matchups, name='all_team_matchups'),
    url(r'^matchup/(?P<matchup_id>\d+)/$', views.matchup, name='matchup'),
    url(r'^standings/$', views.standings, name='standings'),
    url(r'^scoreboard/(?P<week_id>\d+)/$', views.scoreboard, name='scoreboard'),
)