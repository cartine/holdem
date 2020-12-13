from flask import Flask
import GameRunner
app = Flask(__name__)


@app.route('/')
def hello_world():
    GameRunner.run()
    return 'Look at the console'
