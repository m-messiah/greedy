from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from go.models import Game, Task, Code


def index(request):
    active_games = Game.objects.filter(
        end__gte=timezone.now()).order_by('start')[:10]
    return render(request, 'go/index.html', {'active_games': active_games})


def game(request, game_id):
    _game = get_object_or_404(Game, pk=game_id, end__gte=timezone.now())
    try:
        task = _game.task_set.get(pk=request.POST['task_id'])
        code = task.code_set.get(code=request.POST['code'])
    except (KeyError, Task.DoesNotExist, Game.DoesNotExist, Code.DoesNotExist):
        return render(request, 'go/game.html', {
            'game': _game,
            'error_message': "Wrong code"
        })
    else:
        if code.is_posted:
            return render(request, 'go/game.html', {
                'game': _game,
                'error_message': "Code already posted at %s"
                % timezone.localtime(code.post_time)
                .strftime("%H:%M:%S, %d %b %Y")
            })

        else:
            code.is_posted = True
            code.save()
            return render(request, 'go/game.html', {
                'game': _game,
                'error_message': "Code accepted"
            })