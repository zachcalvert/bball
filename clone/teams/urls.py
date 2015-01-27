from django.conf.urls import patterns, url

from teams import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='site_home'),
    url(r'^teams/$', views.all_teams, name='all_teams'),
    url(r'^teams/(?P<team_id>\d+)/$', views.team_profile, name='team_profile'),
    url(r'^teams/(?P<team_id>\d+)/last_month/$', views.team_last_month, name='team_last_month'),
    url(r'^teams/(?P<team_id>\d+)/last_fifteen/$', views.team_last_fifteen, name='team_last_fifteen'),
    url(r'^teams/(?P<team_id>\d+)/last_week/$', views.team_last_week, name='team_last_week'),
)