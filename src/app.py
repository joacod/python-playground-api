"""This is the main entry point for the application."""
from flask import Flask
from services import get_show_info

app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    """Returns a friendly HTTP greeting."""
    return 'Hello, World!'

@app.route('/lyrics/<artist>/<song>')
def lyrics(artist, song):
    """Returns lyrics for a song by an artist."""
    return f'Lyrics for {song} by {artist}'

@app.route('/show/<show_name>')
def show(show_name):
    """Returns show info for a show name."""
    show_info = get_show_info(show_name)
    return show_info
