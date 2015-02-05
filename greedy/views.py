# coding=utf-8
__author__ = 'm_messiah'
from django.shortcuts import render
from django.utils import timezone
from go.models import Game


def index(request):
    active_games = Game.objects.filter(
        end__gte=timezone.now()).order_by('start')[:10]
    return render(request, 'index.html', {'active_games': active_games})
