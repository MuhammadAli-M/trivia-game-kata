from unittest import TestCase

from app.game import Game


class TestGame(TestCase):

    def test_add_a_player_updates_how_many_players_to_1(self):
        game = Game()

        game.add("Muhammad")

        self.assertEqual(game.how_many_players, 1)
