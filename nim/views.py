from flask import (  # pylint: disable=F0401
    jsonify,
    render_template,
    session,
    request,
)

from nim import app
from nim.exceptions import NimException


@app.route('/')
def index():
    return render_template(
        'index.html',
    )


@app.route('/update')
def update_game_state():
    state = session['state']
    bot_move = app.game.chaos.move(state)
    app.game.update(state, bot_move)
    session['state'] = state
    return jsonify({'state': state})


@app.route('/new', methods=['GET', 'POST'])
def new_game():
    """
    route for /new so user can start new game. Uses JSON from frontend
    for params in new game
    """
    try:
        state = app.game.new_game(**request.get_json())
    except NimException as e:
        return jsonify({'error': e.args}), 400
    session['state'] = state
    return jsonify({'state': state})
