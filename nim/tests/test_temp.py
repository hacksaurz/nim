from nim.exceptions import NimException
from nim.game import Nim
import pytest


@pytest.fixture
def game_object():
    game = Nim()
    return game


def test_temp(game_object):
    with pytest.raises(NimException, message="Expecting NimException"):
        game_object.garbage.move([0, 0, 0])
    game_object.garbage.move([0, 0, 0])
