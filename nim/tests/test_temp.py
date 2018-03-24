# pylint: disable=redefined-outer-name
import pytest  # pylint: disable=F0401

from nim.exceptions import NimException
from nim.game import Nim


@pytest.fixture
def game_object():
    game = Nim()
    return game


def test_temp(game_object):
    with pytest.raises(NimException, message="Expecting NimException"):
        game_object.garbage.move([0, 0, 0])
