from flask import Flask

from nim.game import Nim


app = Flask(__name__)
app.secret_key = "super secret key"
app.game = Nim()
