from django.conf.urls import patterns, url

from teams import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='site_home'),
    url(r'^$', views.logout, name='logout'),
    url(r'^teams/(?P<team_id>\d+)/(?P<num_days>\d+)/$', views.team_profile, name='team_profile'),
)