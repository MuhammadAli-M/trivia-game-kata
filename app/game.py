#!/usr/bin/env python3

class Game:
    def __init__(self):
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append("Rock Question %s" % i)

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return True

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player" % self.players[self.current_player])
        print("They have rolled a %s" % roll)

        if self.is_current_player_in_penalty():
            is_even_roll = roll % 2 == 0
            self._update_getting_out_of_penalty(is_even_roll)
            if not is_even_roll:
                self.apply_roll(roll, self.current_player)
            return

        self.apply_roll(roll, self.current_player)

    def _update_getting_out_of_penalty(self, is_even_roll):
        if is_even_roll:
            print("%s is not getting out of the penalty box" % self.players[
                self.current_player])
            self.is_getting_out_of_penalty_box = False
        else:
            print("%s is getting out of the penalty box" % self.players[
                self.current_player])
            self.is_getting_out_of_penalty_box = True

    def is_current_player_in_penalty(self):
        return self.is_player_in_penalty(self.current_player)

    def apply_roll(self, roll, player):
        self.move_player(roll, player)
        print("The category is %s" % self._get_category(player))
        self._ask_question(player)

    def move_player(self, roll, player):
        self.places[player] = self.places[player] + roll
        if self.places[player] > 11:
            self.places[player] = self.places[player] - 12
        print(self.players[player] + '\'s new location is ' + \
              str(self.places[player]))

    def _ask_question(self, player):
        category = self._get_category(player)
        if category == 'Pop': print(self.pop_questions.pop(0))
        if category == 'Science': print(self.science_questions.pop(0))
        if category == 'Sports': print(self.sports_questions.pop(0))
        if category == 'Rock': print(self.rock_questions.pop(0))

    def _get_category(self, player):
        place = self.places[player]
        if place in [0, 4, 8]: return 'Pop'
        if place in [1, 5, 9]: return 'Science'
        if place in [2, 6, 10]: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.is_current_player_in_penalty() and not self.is_getting_out_of_penalty_box:
                self._switch_to_next_player(len(self.players))
                return True

        print("Answer was correct!!!!")
        self.reward_winner(self.current_player)
        winner = self._did_player_win()
        self._switch_to_next_player(len(self.players))
        return winner

    def is_player_in_penalty(self, player):
        return self.in_penalty_box[player]

    def reward_winner(self, current_player):
        self.purses[current_player] += 1
        print(self.players[current_player] + ' now has ' + \
              str(self.purses[current_player]) + ' Gold Coins.')

    def _switch_to_next_player(self, players_count):
        self.current_player = self.current_player + 1
        if self.current_player == players_count: self.current_player = 0

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(self.players[self.current_player] + " was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True

        self._switch_to_next_player(len(self.players))
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] == 6)


from random import randrange

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(randrange(5) + 1)

        if randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner: break