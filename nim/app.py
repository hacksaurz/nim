from flask import (
    jsonify,
    render_template,
    session,
    Flask,
    request,
)
from nim.exceptions import NimException
from nim.game import Nim

app = Flask(__name__)
app.secret_key = 'super secret key'
app.game = Nim()


@app.route('/')
def index():
    return render_template(
        'index.html',
    )


@app.route('/update')
def update_game_state():
    state = session['state']
    # player_move = loads('{"pile": 0, "stones": 1}')
    # app.game.update(state, player_move)
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


if __name__ == '__main__':
    app.run(debug=True)
