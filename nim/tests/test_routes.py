# pylint: disable=redefined-outer-name
import json

import pytest  # pylint: disable=F0401

from nim.app import app
from nim.game import (
    NUM_LIMIT_MIN,
    NUM_LIMIT_MAX,
    DEFAULT_MIN,
    DEFAULT_MAX,
    DEFAULT_PILES,
)


@pytest.fixture(scope="module")
def client_app():
    return app.test_client()


@pytest.mark.parametrize("request", [
    # With valid min, max and piles
    {'min': 5, 'max': 15, 'piles': 4},
    # Without min
    {'max': 15, 'piles': 4},
    # Without max
    {'min': 5, 'piles': 4},
    # Without piles
    {'min': 5, 'max': 15},
    # Without any arguments
    {},
    # Max out the number of stones per pile
    {'min': NUM_LIMIT_MAX, 'max': NUM_LIMIT_MAX},
    # Max out the number of piles
    {'piles': NUM_LIMIT_MAX},
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
    assert request.get('piles', DEFAULT_PILES) == len(state)
    # Check that min value was respected
    assert NUM_LIMIT_MIN <= request.get('min', DEFAULT_MIN) <= min(state)
    # Check that max value was respected
    assert max(state) <= request.get('max', DEFAULT_MAX) <= NUM_LIMIT_MAX


@pytest.mark.parametrize("request", [
    # Too big value for min (passing max to satisfy min <= max)
    {'min': NUM_LIMIT_MAX + 1, 'max': NUM_LIMIT_MAX + 1},
    # Too big value for max
    {'max': NUM_LIMIT_MAX + 1},
    # Too big value for piles
    {'piles': NUM_LIMIT_MAX + 1},
    # Too small value for min
    {'min': NUM_LIMIT_MIN - 1},
    # Too small value for max
    {'max': NUM_LIMIT_MIN - 1},
    # Too small value for piles
    {'piles': NUM_LIMIT_MIN - 1},
    # Non int value for min
    {'min': "a"},
    # Non int value for max
    {'max': "a"},
    # Non int value for piles
    {'piles': "a"},
    # min greater than max
    {'min': 30, 'max': 10},
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
    Ensures DEFAULT constants for min, max & piles are in between min limit &
    max limit constants
    """
    assert all(NUM_LIMIT_MIN <= x <= NUM_LIMIT_MAX
               for x in (DEFAULT_MIN, DEFAULT_MAX, DEFAULT_PILES))


def test_index(client_app):
    """
    Ensures we can load the app
    """
    response = client_app.get('/', content_type='html/text')
    assert response.status_code == 200
