from django.conf.urls import patterns, url
from teams import urls
from schedule import views

urlpatterns = patterns('',
    url(r'^(?P<team_id>\d+)/$', views.current_matchup, name='current_matchup'),
    url(r'^all_matchups/(?P<team_id>\d+)/$', views.all_matchups, name='all_matchups'),
)