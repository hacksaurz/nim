from flask import (
    jsonify,
    render_template,
    session,
    Flask,
)
from json import loads

from game import Game


app = Flask(__name__)
app.secret_key = 'super secret key'
app.game = Game()


@app.route('/')
def index():
    json = loads('{"min": 3, "max": 12, "piles": 3}')
    session['state'] = app.game.new_game(
        min=json['min'],
        max=json['max'],
        piles=json['piles'],
    )
    return render_template(
        'index.html',
        state=session['state']
    )


@app.route('/update')
def update_game_state():
    new_state = session['state']  # minus player move from json
    session['state'] = app.game.random.move(new_state)
    return jsonify({'state': session['state']})


if __name__ == '__main__':
    app.run(debug=True)
