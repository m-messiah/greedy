from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from random import randint
import datetime
from go.models import *


def create_game(game_name, start, end):
    """
    Creates a game with given `name` started at `start`
    and ends at `end`.
    :param game_name: string
    :param start: datetime
    :param end: datetime
    :return: Game
    """
    return Game.objects.create(name=game_name, author='tester',
                               legend="Welcome to %s" % game_name, prikvel='-',
                               start=start, end=end)


class GoViewTests(TestCase):
    def test_index_with_no_games(self):
        """
        If no games exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('go:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no planned games")
        self.assertQuerysetEqual(response.context["active_games"], [])

    def test_index_with_inactive_game(self):
        """
        Games with end in past should not be displayed on the index page.
        """
        create_game("Past game",
                    timezone.now() - datetime.timedelta(days=2),
                    timezone.now() - datetime.timedelta(hours=1)
        )
        response = self.client.get(reverse('go:index'))
        self.assertContains(response,
                            "There are no planned games", status_code=200)
        self.assertQuerysetEqual(response.context["active_games"], [])

    def test_index_with_active_game(self):
        """
        Valid games should be displayed on the index page.
        """
        create_game("New game",
                    timezone.now() + datetime.timedelta(days=1),
                    timezone.now() + datetime.timedelta(days=2)
        )
        response = self.client.get(reverse('go:index'))
        self.assertQuerysetEqual(response.context["active_games"],
                                 ['<Game: New game>'])

    def test_index_with_active_and_inactive_games(self):
        """
        Valid games should be displayed on the index page.
        """
        create_game("New game",
                    timezone.now() + datetime.timedelta(days=1),
                    timezone.now() + datetime.timedelta(days=2)
        )
        create_game("Past game",
                    timezone.now() - datetime.timedelta(days=2),
                    timezone.now() - datetime.timedelta(hours=1)
        )
        response = self.client.get(reverse('go:index'))
        self.assertQuerysetEqual(response.context["active_games"],
                                 ['<Game: New game>'])

    def test_index_with_two_active_games(self):
        """
        Valid games should be displayed on the index page.
        """
        create_game("New game 1",
                    timezone.now() + datetime.timedelta(days=1),
                    timezone.now() + datetime.timedelta(days=2)
        )
        create_game("New game 2",
                    timezone.now() + datetime.timedelta(days=2),
                    timezone.now() + datetime.timedelta(days=3)
        )
        response = self.client.get(reverse('go:index'))
        self.assertQuerysetEqual(response.context["active_games"],
                                 ['<Game: New game 1>', '<Game: New game 2>'])


class GameViewTests(TestCase):
    def test_game_view_with_inactive_game(self):
        """
        The game view of inactive game should return a 404 not found
        """
        inactive_game = create_game(
            "Past game",
            timezone.now() - datetime.timedelta(days=2),
            timezone.now() - datetime.timedelta(hours=1)
        )
        response = self.client.get(reverse('go:game',
                                           args=(inactive_game.id, )))
        self.assertEqual(response.status_code, 404)

    def test_game_view_with_active_game(self):
        """
        The game view of active game should return game
        """
        active_game = create_game(
            "New game",
            timezone.now() + datetime.timedelta(days=1),
            timezone.now() + datetime.timedelta(days=2)
        )
        response = self.client.get(reverse('go:game',
                                           args=(active_game.id, )))
        self.assertContains(response, active_game.name, status_code=200)