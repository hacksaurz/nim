from flask import (
    jsonify,
    render_template,
    session,
    Flask,
)
from json import loads

from game import Nim


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
    json = loads('{"min": 3, "max": 12, "piles": 3}')
    state = app.game.new_game(
        min=json['min'],
        max=json['max'],
        piles=json['piles'],
    )
    session['state'] = state
    return jsonify({'state': state})


if __name__ == '__main__':
    app.run(debug=True)
