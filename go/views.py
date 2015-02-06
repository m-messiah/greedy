from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from go.models import Game, Task, Code
from django.utils.translation import ugettext as _


def game(request, game_id):
    _game = get_object_or_404(Game, pk=game_id, end__gte=timezone.now())
    if request.method == 'GET':
        error_message = None
    elif request.method == 'POST':
        try:
            task = _game.task_set.get(pk=request.POST['task_id'])
            code = task.code_set.get(code=request.POST['code'])
        except (KeyError, Task.DoesNotExist, Game.DoesNotExist, Code.DoesNotExist):
            error_message = 1, _("Wrong code")
        else:
            if code.is_posted:
                error_message = (1, _("Code already posted at %s"
                                 % timezone.localtime(code.post_time)
                                 .strftime("%H:%M:%S, %d %b %Y")))
            else:
                code.is_posted = True
                code.save()
                error_message = 0, _("Code accepted")
    else:
        error_message = 1, _("Invalid request")

    return render(request, 'go/index.html', {'game': _game,
                                             'error_message': error_message})