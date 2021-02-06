from flask import Flask, render_template
from games import games

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', title="Nintendon't", games=games)


@app.route('/about')
def about():
    return 'About us'


@app.route('/games/<int:game_id>')
def get_game(game_id):
    return f'Game #{game_id}'


if __name__ == '__main__':
    app.run()
