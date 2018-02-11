from flask import (
    jsonify,
    render_template,
    Flask,
)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update')
def update_game_state():
    return jsonify({})


if __name__ == '__main__':
    app.run(debug=True)
