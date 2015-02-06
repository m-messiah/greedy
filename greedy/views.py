# coding=utf-8
from django.contrib.auth import authenticate, login

from django.utils.translation import ugettext as _
__author__ = 'm_messiah'
from django.shortcuts import render
from django.utils import timezone
from go.models import Game


def index(request):
    error_message = None
    active_games = Game.objects.filter(
        end__gte=timezone.now()).order_by('start')[:10]
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                print("Logined")
            else:
                error_message = 1, _('Disabled user')
        else:
            error_message = 1, _('Invalid user')
    return render(request, 'index.html', {'active_games': active_games,
                                          'error_message': error_message})