import pytest
from python3.trivia import Game


@pytest.fixture
def game():
    return Game()
