from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.utils.translation import force_text
from go.models import Game, Task, Code, Player
from django.utils.translation import ugettext as _
from django.template.defaultfilters import date as _date
from django.contrib.auth.decorators import login_required


@login_required
def game(request, game_id):
    now = timezone.now()
    _game = get_object_or_404(Game, pk=game_id, end__gte=now)
    if _game.start > now:
        return render(
            request, 'go/early.html',
            {'game': _game,
             'error_message': (1, " ".join(map(
                 force_text,
                 (_("Game will start at"),
                  _date(_game.start, "G:i:s j M Y"),
                  "<br>",
                  _('Now it is only'),
                  _date(now, "G:i:s j M Y")))))})

    try:
        task = request.user.player.current_task
    except:
        player = Player(user=request.user,
                        current_task=_game.task_set.get(game=_game, num=1))
        player.save()
    finally:
        task = request.user.player.current_task

        next = True
        for code in task.code_set.all():
            if not code.is_posted:
                next = False
        if next:
            task = request.user.player.current_task = _game.task_set.get(
                game=_game, num=(task.num + 1))
            request.user.player.save()

        if request.method == 'GET':
            error_message = None
        elif request.method == 'POST':
            try:
                code = task.code_set.get(code=request.POST['code'].lower())
            except (KeyError, Task.DoesNotExist,
                    Game.DoesNotExist, Code.DoesNotExist):
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
                    next = True
                    for code in task.code_set.all():
                        if not code.is_posted:
                            next = False
                    if next:
                        task = request.user.player.current_task = _game.task_set.get(
                            game=_game, num=(task.num + 1))
                        request.user.player.save()

        else:
            error_message = 1, _("Invalid request")

        return render(request, 'go/index.html', {'game': _game, 'task': task,
                                                 'error_message': error_message})