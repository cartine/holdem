from flask import Flask
import GameRunner
app = Flask(__name__)


@app.route('/')
def hello_world():
    GameRunner.run()
    return 'Look at the console'


@app.route('/sayhitogreg')
def hello_world2():
    # GameRunner.run()
    return 'Hi Greg'


