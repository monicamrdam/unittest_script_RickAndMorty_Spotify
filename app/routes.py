from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def home():
    message = {
        "Home": 'http://127.0.0.1:8080/',
        "Artist": 'http://127.0.0.1:8080/artist?name=',
        "Character": 'http://127.0.0.1:8080/character',
        "Episode": 'http://127.0.0.1:8080/episode',
        "Favourites": 'http://127.0.0.1:8080/favourites',

    }
    return jsonify(message)
