from django.conf.urls import patterns, url

from teams import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='site_home'),
    url(r'^teams/$', views.all_teams, name='all_teams'),
    url(r'^teams/(?P<team_id>\d+)/$', views.team_profile, name='team_profile'),
)