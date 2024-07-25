from unittest import TestCase

from app.game import Game


class TestGame(TestCase):

    def test_add_a_player_updates_how_many_players_to_1(self):
        game = Game()

        game.add("Muhammad")

        self.assertEqual(game.how_many_players, 1)

    def test_add_two_players_append_two_players(self):
        game = Game()

        game.add("Muhammad")
        game.add("Adam")

        self.assertEqual(game.how_many_players, 2)

    def test_wrong_answer_sets_player_in_penalty(self):
        game = Game()
        game.add('Chet')
        game.add('Pat')
        game.add('Sue')

        game.roll(1)
        player = game.current_player
        game.wrong_answer()

        self.assertEqual(game.is_player_in_penalty(player), True)

    def test_roll_1_after_roll_1_and_wrong_answer_does_not_cancel_penalty(self):
        game = Game()
        game.add('Chet')
        game.add('Pat')

        game.roll(1)
        game.wrong_answer()
        game.roll(1)

        self.assertEqual(game.is_getting_out_of_penalty_box, False)

    def test_roll_1_after_roll_1_and_correct_answer_does_not_cancel_penalty(self):
        game = Game()
        game.add('Chet')
        game.add('Pat')

        game.roll(1)
        game.was_correctly_answered()
        game.roll(1)

        self.assertEqual(game.is_getting_out_of_penalty_box, False)

    def test_roll_1_after_correct_answer_after_wrong_answer_does_cancel_penalty(
            self):
        game = Game()
        game.add('Chet')
        game.add('Pat')

        game.roll(1)
        game.wrong_answer()
        game.roll(1)
        game.was_correctly_answered()
        game.roll(1)

        self.assertEqual(game.is_getting_out_of_penalty_box, True)