from django.conf.urls import patterns, url
from players import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='players_home'),
    url(r'^all/$', views.all_totals, name='all_totals'),
    url(r'^all_avg/$', views.all_averages, name='all_averages'),
    url(r'^(?P<player_id>\d+)/$', views.player_profile, name='player_profile'),
)