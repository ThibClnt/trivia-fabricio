from python3.trivia import Game
from python3.tests.config import game


def test_when_no_players_then_game_is_not_playable(game):
    assert not game.is_playable()


def test_when_less_than_two_players_then_game_is_not_playable(game):
    game.add('P1')
    assert not game.is_playable()


def test_when_two_players_or_more_then_game_is_playable(game):
    game.add('P1')
    game.add('P2')
    assert game.is_playable()


def test_add_player():
    game = Game()
    assert game.add("Player1")
    assert game.add("Player2")
    assert game.how_many_players == 2
    assert game.players[0].name == "Player1"
    assert game.players[1].name == "Player2"


def test_roll_movement(game):
    game.add("Player1")
    game.roll(3)
    assert game.places[0] == 3


def test_correct_answer(game):
    game.add("Player1")
    game.was_correctly_answered()
    assert game.purses[0] == 1


def test_wrong_answer(game):
    game.add("Player1")
    game.wrong_answer()
    assert game.in_penalty_box[0]


def test_win_condition(game):
    game.add("Player1")
    for _ in range(6):
        game.was_correctly_answered()
    assert not game._did_player_win()
