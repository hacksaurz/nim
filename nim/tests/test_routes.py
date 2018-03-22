import json

import pytest

from nim.game import (
    DEFAULT_MIN,
    DEFAULT_MAX,
    DEFAULT_PILES
)

from nim.app import app


@pytest.fixture
def client_app():
    return app.test_client()


def assert_new_game_success(passed_client, req):
    """
    Asserts post to /new is 200
    & state is not empty
    Checks piles is in line with req &
    none in response lower than mix or
    higher than max
    :param passed_client: test_client
    :param req: Desired game conditions
    """
    response = passed_client.post(
        '/new',
        content_type='application/json',
        data=req
    )
    assert response.status_code == 200
    response = json.loads(response.data)
    request = json.loads(req)
    assert 'state' in response
    state = response['state']
    assert all(isinstance(x, int) for x in state)
    assert request.get('piles', DEFAULT_PILES) == len(state)
    assert request.get('min', DEFAULT_MIN) <= min(state) <= max(state)
    request.get('max', DEFAULT_MAX)


def assert_new_game_failed(passed_client, req):
    """
    Asserts post tp /new gets error code 400
    & the string 'error' exists in the response
    :param passed_client: test_client
    :param req: json to post
    """
    response = passed_client.post(
        '/new',
        content_type='application/json',
        data=req
    )
    assert response.status_code == 400
    assert 'error' in json.loads(response.data) and json.loads(response.data)['error']
    assert 'state' not in json.loads(response.data)


def test_index(client_app):
    response = client_app.get('/', content_type='html/text')
    assert response.status_code == 200


def test_new_success(client_app):
    assert_new_game_success(client_app,
                            json.dumps({'min': 5, 'max': 15, 'piles': 4}))


def test_new_omit_min_success(client_app):
    assert_new_game_success(client_app,
                            json.dumps({'max': 15, 'piles': 4}))


def test_new_omit_max_success(client_app):
    assert_new_game_success(client_app,
                            json.dumps({'min': 5, 'piles': 4}))


def test_new_omit_piles_success(client_app):
    assert_new_game_success(client_app,
                            json.dumps({'min': 5, 'max': 15}))


def test_new_omit_all_success(client_app):
    assert_new_game_success(client_app,
                            json.dumps({}))


def test_new_nums_limit_success(client_app):
    assert_new_game_success(client_app,
                            json.dumps({'min': 50, 'max': 50}))


def test_new_piles_limit_success(client_app):
    assert_new_game_success(client_app,
                            json.dumps({'piles': 5}))


def test_new_max_limit_fail(client_app):
    assert_new_game_failed(client_app,
                           json.dumps({'min': 10, 'max': 51, 'piles': 3}))


def test_new_piles_limit_fail(client_app):
    assert_new_game_failed(client_app,
                           json.dumps({'min': 10, 'max': 10, 'piles': 51}))


def test_new_min_limit_fail(client_app):
    assert_new_game_failed(client_app,
                           json.dumps({'min': 51, 'max': 51, 'piles': 4}))


def test_new_pile_zero_fail(client_app):
    assert_new_game_failed(client_app,
                           json.dumps({'min': 10, 'max': 20, 'piles': 0}))


def test_new_min_zero_fail(client_app):
    assert_new_game_failed(client_app,
                           json.dumps({'min': 0, 'max': 20, 'piles': 4}))


def test_new_max_zero_fail(client_app):
    assert_new_game_failed(client_app,
                           json.dumps({'min': 5, 'max': 0, 'piles': 4}))


def test_min_greater_than_max_fail(client_app):
    assert_new_game_failed(client_app,
                           json.dumps({'min': 30, 'max': 10, 'piles': 4}))


def test_new_non_int_pile_fail(client_app):
    assert_new_game_failed(client_app,
                           json.dumps({'min': 10, 'max': 20, 'piles': "a"}))


def test_new_non_int_min_fail(client_app):
    assert_new_game_failed(client_app,
                           json.dumps({'min': "S", 'max': 20, 'piles': 4}))


def test_new_non_int_max_fail(client_app):
    assert_new_game_failed(client_app,
                           json.dumps({'min': 10, 'max': "F", 'piles': 4}))
