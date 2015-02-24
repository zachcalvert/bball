from django.conf.urls import patterns, url
from teams import urls
from players import views

urlpatterns = patterns('',
    url(r'^free_agents/(?P<num_days>\d+)/$', views.free_agents, name='free_agents'),
    url(r'^free_agents/add/(?P<player_id>\d+)/$', views.add_player, name='add_player_page'),
    url(r'^(?P<player_id>\d+)/(?P<num_days>\d+)/$', views.player_profile, name='player_profile'),
)