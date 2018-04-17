import json

import pytest

from nim.app import app
from nim.game import (
    NUM_LIMIT_MIN,
    NUM_LIMIT_MAX,
    DEFAULT_MIN,
    DEFAULT_MAX,
    DEFAULT_PILES,
)


@pytest.fixture
def client_app():
    return app.test_client()


def assert_new_game_success(client, request):
    """
    Asserts post to /new gets 200 & state is not empty. Checks response state
    is in line with request. Uses arguments passed or DEFAULT
    :param client: test_client
    :param request: Desired game conditions
    """
    response = client.post(
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


def assert_new_game_failed(client, request):
    """
    Asserts post to new_game route 400, the string 'error' is in the response
    and response isn't empty
    :param client: test_client
    :param request: json to post
    """
    response = client.post(
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
    response = client_app.get('/', content_type='html/text')
    assert response.status_code == 200


def test_new_success(client_app):
    assert_new_game_success(client_app, {'min': 5, 'max': 15, 'piles': 4})


def test_new_omit_min_success(client_app):
    assert_new_game_success(client_app, {'max': 15, 'piles': 4})


def test_new_omit_max_success(client_app):
    assert_new_game_success(client_app, {'min': 5, 'piles': 4})


def test_new_omit_piles_success(client_app):
    assert_new_game_success(client_app, {'min': 5, 'max': 15})


def test_new_omit_all_success(client_app):
    assert_new_game_success(client_app, {})


def test_new_nums_limit_success(client_app):
    assert_new_game_success(client_app, {'min': 50, 'max': 50})


def test_new_piles_limit_success(client_app):
    assert_new_game_success(client_app, {'piles': 5})


def test_new_max_limit_fail(client_app):
    assert_new_game_failed(client_app, {'max': 51})


def test_new_piles_limit_fail(client_app):
    assert_new_game_failed(client_app, {'piles': 51})


def test_new_min_limit_fail(client_app):
    assert_new_game_failed(client_app, {'min': 51, 'max': 51})


def test_new_pile_zero_fail(client_app):
    assert_new_game_failed(client_app, {'piles': 0})


def test_new_min_zero_fail(client_app):
    assert_new_game_failed(client_app, {'min': 0})


def test_new_max_zero_fail(client_app):
    assert_new_game_failed(client_app, {'max': 0})


def test_min_greater_than_max_fail(client_app):
    assert_new_game_failed(client_app, {'min': 30, 'max': 10})


def test_new_non_int_pile_fail(client_app):
    assert_new_game_failed(client_app, {'piles': "a"})


def test_new_non_int_min_fail(client_app):
    assert_new_game_failed(client_app, {'min': "S"})


def test_new_non_int_max_fail(client_app):
    assert_new_game_failed(client_app, {'max': "F"})
