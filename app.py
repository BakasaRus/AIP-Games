from flask import Flask, render_template, request
from games import games, find_by_name

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', title="Nintendon't", games=games)


@app.route('/games/<int:game_id>')
def get_game(game_id):
    return render_template('game.html', game=games[game_id])


@app.route('/search')
def search():
    name = request.args.get('title', '')
    return render_template('index.html', title="Nintendon't", games=find_by_name(name))


if __name__ == '__main__':
    app.run()
