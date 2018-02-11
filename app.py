from flask import (
    jsonify,
    render_template,
    Flask,
)
from json import loads

from game import Game


app = Flask(__name__)
app.game = Game()


@app.route('/')
def index():
    state = app.game.new_game(
        min=3,
        max=12,
        piles=3,
    )
    return render_template('index.html', state=state)


@app.route('/update')
def update_game_state():
    # some game state that we get from front end
    old_state = loads('{"state": [6, 6, 6]}')['state']
    new_state = {
        'state': app.game.random.move(old_state)
    }

    return jsonify(new_state)


if __name__ == '__main__':
    app.run(debug=True)
