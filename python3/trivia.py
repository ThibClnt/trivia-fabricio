#!/usr/bin/env python3

class Player:
    def __init__(self, name):
        self.name = name
        self.place = 0
        self.purse = 0
        self.in_penalty_box = False

    def __str__(self):
        return self.name


class Game:
    def __init__(self):
        self.players = []

        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []

        self.current_player_index = 0
        self.is_getting_out_of_penalty_box = False

        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            self.rock_questions.append(self.create_rock_question(i))

    @property
    def current_player(self):
        return self.players[self.current_player_index]

    def create_rock_question(self, index):
        return "Rock Question %s" % index

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        player = Player(player_name)
        self.players.append(player)

        print(player_name + " was added")
        print("They are player number %s" % len(self.players))

        return player

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print(f"{self.current_player} is the current player")
        print("They have rolled a %s" % roll)

        if self.current_player.in_penalty_box:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.current_player)
                self._do_roll(roll)
            else:
                print("%s is not getting out of the penalty box" % self.current_player)
                self.is_getting_out_of_penalty_box = False
        else:
            self._do_roll(roll)

    def _do_roll(self, roll):
        self.current_player.place += roll
        if self.current_player.place > 11:
            self.current_player.place -= 12

        print(f"{self.current_player}'s new location is {self.current_player.place}")
        print(f"The category is {self._current_category}")
        self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))

    @property
    def _current_category(self):
        if self.current_player.place == 0: return 'Pop'
        if self.current_player.place == 4: return 'Pop'
        if self.current_player.place == 8: return 'Pop'
        if self.current_player.place == 1: return 'Science'
        if self.current_player.place == 5: return 'Science'
        if self.current_player.place == 9: return 'Science'
        if self.current_player.place == 2: return 'Sports'
        if self.current_player.place == 6: return 'Sports'
        if self.current_player.place == 10: return 'Sports'
        return 'Rock'

    def was_correctly_answered(self):
        if self.current_player.in_penalty_box:
            if self.is_getting_out_of_penalty_box:
                return self._award_points_and_check_winner()
            else:
                self.current_player_index += 1
                if self.current_player_index == len(self.players):
                    self.current_player_index = 0
                return True

        else:
            return self._award_points_and_check_winner()

    def _award_points_and_check_winner(self):
        print("Answer was correct!!!!")
        self.current_player.purse += 1
        print(f"{self.current_player} now has {self.current_player.purse} Gold Coins.")

        winner = self._did_player_win()
        self.current_player_index += 1
        if self.current_player_index == len(self.players): self.current_player_index = 0

        return winner

    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(f"{self.current_player} was sent to the penalty box")
        self.current_player.in_penalty_box = True

        self.current_player_index += 1
        if self.current_player_index == len(self.players): self.current_player_index = 0
        return True

    def _did_player_win(self):
        return not self.current_player.purse == 6


if __name__ == '__main__':
    from random import randrange

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

        if not not_a_winner:
            break
