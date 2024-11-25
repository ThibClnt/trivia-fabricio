import random

from python3.trivia import Game


def test_golden_master(capsys):
    random.seed(42)

    game = Game()

    game.add('Chet')
    game.add('Pat')
    game.add('Sue')

    while True:
        game.roll(random.randrange(5) + 1)

        if random.randrange(9) == 7:
            not_a_winner = game.wrong_answer()
        else:
            not_a_winner = game.was_correctly_answered()

        if not not_a_winner:
            break

    output = capsys.readouterr().out

    with open("golden_master_output.txt", "r") as file:
        expected_output = file.read()

    assert output == expected_output
