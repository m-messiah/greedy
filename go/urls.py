# coding=utf-8
__author__ = 'm_messiah'
from django.conf.urls import patterns, url

from go import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<game_id>\d+)/$', views.game, name='game')
)