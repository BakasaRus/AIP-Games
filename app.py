from flask import Flask, render_template, request, abort
from games import games, find_by_name
from models import db, User
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def homepage():
    return render_template('index.html', title="Nintendon't", games=games)


@app.route('/games/<int:game_id>')
def get_game(game_id):
    if game_id not in games:
        abort(404)
    return render_template('game.html', game=games[game_id])


@app.route('/search')
def search():
    name = request.args.get('title', '')
    return render_template('index.html', title="Nintendon't", games=find_by_name(name))


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()
