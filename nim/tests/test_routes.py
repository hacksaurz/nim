# pylint: disable=redefined-outer-name
import json

import pytest  # pylint: disable=F0401

from nim import app
from nim.game import (
    ABS_MIN_STONES_PER_PILE,
    ABS_MAX_STONES_PER_PILE,
    ABS_MIN_NUM_PILES,
    ABS_MAX_NUM_PILES,
    DEFAULT_MIN_STONES_PER_PILE,
    DEFAULT_MAX_STONES_PER_PILE,
    DEFAULT_NUM_PILES,
)


@pytest.fixture(scope="module")
def client_app():
    return app.test_client()


@pytest.mark.parametrize("request", [
    # With valid min_stones_per_pile, max_stones_per_pile and num_piles
    {'min_stones_per_pile': 5, 'max_stones_per_pile': 15, 'num_piles': 4},
    # Without min_stones_per_pile
    {'max_stones_per_pile': 15, 'num_piles': 4},
    # Without max_stones_per_pile
    {'min_stones_per_pile': 5, 'num_piles': 4},
    # Without num_piles
    {'min_stones_per_pile': 5, 'max_stones_per_pile': 15},
    # Without any arguments
    {},
    # Max out the number of stones per pile
    {'min_stones_per_pile': ABS_MAX_STONES_PER_PILE,
     'max_stones_per_pile': ABS_MAX_STONES_PER_PILE},
    # Max out the number of piles
    {'num_piles': ABS_MAX_NUM_PILES},
    # Minimum number of stones per pile
    {'min_stones_per_pile': ABS_MIN_STONES_PER_PILE,
     'max_stones_per_pile': ABS_MIN_STONES_PER_PILE},
    # Minimum number of piles
    {'num_piles': ABS_MIN_NUM_PILES},
])
def test_new_game_success(client_app, request):
    """
    Asserts post to /new gets 200 & state is not empty. Checks response state
    is in line with request. Uses arguments passed or DEFAULT
    :param client_app: test_client
    :param request: Desired game conditions
    """
    response = client_app.post(
        '/new',
        content_type='application/json',
        data=json.dumps(request)
    )
    assert response.status_code == 200
    response = json.loads(response.data.decode("utf-8"))
    assert 'state' in response
    state = response['state']
    assert all(isinstance(x, int) for x in state)
    # Checking num piles returned is requested or default
    assert request.get('num_piles', DEFAULT_NUM_PILES) == len(state)
    # Check that min_stones_per_pile value was respected
    min_stones_per_pile = request.get('min_stones_per_pile',
                                      DEFAULT_MIN_STONES_PER_PILE)
    assert ABS_MIN_STONES_PER_PILE <= min_stones_per_pile <= min(state)
    # Check that max_stones_per_pile value was respected
    max_stones_per_pile = request.get('max_stones_per_pile',
                                      DEFAULT_MAX_STONES_PER_PILE)
    assert max(state) <= max_stones_per_pile <= ABS_MAX_STONES_PER_PILE


@pytest.mark.parametrize("request", [
    # Too big value for min_stones_per_pile (passing max_stones_per_pile to
    # satisfy min_stones_per_pile <= max_stones_per_pile)
    {'min_stones_per_pile': ABS_MAX_STONES_PER_PILE + 1,
     'max_stones_per_pile': ABS_MAX_STONES_PER_PILE + 1},
    # Too big value for max_stones_per_pile
    {'max_stones_per_pile': ABS_MAX_STONES_PER_PILE + 1},
    # Too big value for num_piles
    {'num_piles': ABS_MAX_NUM_PILES + 1},
    # Too small value for min_stones_per_pile
    {'min_stones_per_pile': ABS_MIN_STONES_PER_PILE - 1},
    # Too small value for max_stones_per_pile
    {'max_stones_per_pile': ABS_MIN_STONES_PER_PILE - 1},
    # Too small value for num_piles
    {'num_piles': ABS_MIN_NUM_PILES - 1},
    # Non int value for min_stones_per_pile
    {'min_stones_per_pile': "a"},
    # Non int value for max_stones_per_pile
    {'max_stones_per_pile': "a"},
    # Non int value for num_piles
    {'num_piles': "a"},
    # min_stones_per_pile greater than max_stones_per_pile
    {'min_stones_per_pile': 30, 'max_stones_per_pile': 10},
])
def test_new_game_failed(client_app, request):
    """
    Asserts post to new_game route 400, the string 'error' is in the response
    and response isn't empty
    :param client_app: test_client
    :param request: json to post
    """
    response = client_app.post(
        '/new',
        content_type='application/json',
        data=json.dumps(request)
    )
    assert response.status_code == 400
    response = json.loads(response.data.decode("utf-8"))
    assert 'error' in response and response['error']
    assert 'state' not in response


def test_constants():
    """
    Ensures DEFAULT constants for min_stones_per_pile, max_stones_per_pile &
    num_piles are within their absolute limits
    """
    assert all(ABS_MIN_STONES_PER_PILE <= x <= ABS_MAX_STONES_PER_PILE
               for x in (DEFAULT_MIN_STONES_PER_PILE,
                         DEFAULT_MAX_STONES_PER_PILE))
    assert ABS_MIN_NUM_PILES <= DEFAULT_NUM_PILES <= ABS_MAX_NUM_PILES


def test_index(client_app):
    """
    Ensures we can load the app
    """
    response = client_app.get('/', content_type='html/text')
    assert response.status_code == 200
