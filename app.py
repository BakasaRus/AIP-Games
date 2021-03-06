from flask import Flask, render_template, request, abort
from games import find_by_name
from models import db, User, Game, Review
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def homepage():
    games = Game.query.all()
    return render_template('index.html', title="Nintendon't", games=games)


@app.route('/games/<int:game_id>')
def get_game(game_id):
    game = Game.query.filter_by(id=game_id).first_or_404()
    return render_template('game.html', game=game)


@app.route('/search')
def search():
    name = request.args.get('title', '')
    return render_template('index.html', title="Nintendon't", games=find_by_name(name))


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()
