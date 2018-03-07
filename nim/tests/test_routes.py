from nim.app import app
import pytest
import json


@pytest.fixture
def test_app():
    return app.test_client()


def test_index(test_app):
    response = test_app.get('/', content_type='html/text')
    assert response.status_code == 200


def test_new_success(test_app):
    new_game_response = test_app.post(
        '/new',
        data='{"min": 10, "max": 10, "piles": 4}',
        content_type='application/json'
    )
    expected_json = {"state": [10, 10, 10, 10]}
    assert json.loads(new_game_response.data) == expected_json


def test_new_max_limit_fail(test_app):
    new_game_response = test_app.post(
        '/new',
        data='{"min": 10, "max": 51, "piles": 4}',
        content_type='application/json'
    )
    expected_json = {"error": ["Please use integers between 1 and 50"]}
    assert json.loads(new_game_response.data) == expected_json


def test_new_piles_limit_fail(test_app):
    new_game_response = test_app.post(
        '/new',
        data='{"min": 10, "max": 10, "piles": 51}',
        content_type='application/json'
    )
    expected_json = {"error": ["Please use integers between 1 and 50"]}
    assert json.loads(new_game_response.data) == expected_json


def test_new_all_limit_fail(test_app):
    new_game_response = test_app.post(
        '/new',
        data='{"min": 51, "max": 51, "piles": 51}',
        content_type='application/json'
    )
    expected_json = {"error": ["Please use integers between 1 and 50"]}
    assert json.loads(new_game_response.data) == expected_json


def test_new_pile_zero_fail(test_app):
    new_game_response = test_app.post(
        '/new',
        data='{"min": 10, "max": 20, "piles": 0}',
        content_type='application/json'
    )
    expected_json = {"error": ["Please use integers between 1 and 50"]}
    assert json.loads(new_game_response.data) == expected_json


def test_new_all_zero_fail(test_app):
    new_game_response = test_app.post(
        '/new',
        data='{"min": 0, "max": 0, "piles": 0}',
        content_type='application/json'
    )
    expected_json = {"error": ["Please use integers between 1 and 50"]}
    assert json.loads(new_game_response.data) == expected_json


def test_min_greater_than_max_fail(test_app):
    new_game_response = test_app.post(
        '/new',
        data='{"min": 30, "max": 10, "piles": 4}',
        content_type='application/json'
    )
    expected_json = {"error": ["Min(30) cant be greater than Max(10)"]}
    assert json.loads(new_game_response.data) == expected_json


def test_new_non_int_pile_fail(test_app):
    new_game_response = test_app.post(
        '/new',
        data='{"min": 0, "max": 10, "piles": "a"}',
        content_type='application/json'
    )
    expected_json = {"error": ["Please use integers between 1 and 50"]}
    assert json.loads(new_game_response.data) == expected_json


def test_new_non_int_all_fail(test_app):
    new_game_response = test_app.post(
        '/new',
        data='{"min": "S", "max": "M", "piles": "D"}',
        content_type='application/json'
    )
    expected_json = {"error": ["Please use integers between 1 and 50"]}
    assert json.loads(new_game_response.data) == expected_json
