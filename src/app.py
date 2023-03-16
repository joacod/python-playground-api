# This is the main entry point for the application

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/lyrics/<artist>/<song>')
def lyrics(artist, song):
    return 'Lyrics for %s by %s' % (song, artist)
