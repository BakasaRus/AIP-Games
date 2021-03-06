from flask import Flask, render_template, request, abort, redirect, url_for
from models import db, Game, User, Review
from flask_migrate import Migrate
from forms import LoginForm, RegisterForm, ReviewForm, GameForm
from flask_login import login_user, logout_user, LoginManager, login_required, current_user
import locale
from os import environ

locale.setlocale(locale.LC_ALL, '')
app = Flask(__name__)
app.secret_key = environ['APP_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)
login_manager = LoginManager(app)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def homepage():
    games = Game.query.all()
    return render_template('index.html', title="Nintendon't", games=games)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember_me = form.remember_me.data
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            abort(401)
        login_user(user, remember=remember_me)
        return redirect(url_for('homepage'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            abort(400)
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User(email=email, first_name=first_name, last_name=last_name)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/games/new', methods=['GET', 'POST'])
@login_required
def create_game():
    form = GameForm()
    if form.validate_on_submit():
        game = Game(title=form.title.data,
                    desc=form.desc.data,
                    poster=form.poster.data,
                    release_date=form.release_date.data,
                    price=form.price.data,
                    on_sale=form.on_sale.data)
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('get_game', game_id=game.id))
    return render_template('new_game.html', form=form)


@app.route('/games/<int:game_id>')
def get_game(game_id):
    game = Game.query.filter_by(id=game_id).first_or_404()
    review_form = ReviewForm()
    return render_template('game.html', game=game, form=review_form)


@app.route('/games/<int:game_id>/reviews', methods=['POST'])
def create_review(game_id):
    review_form = ReviewForm()
    print(type(review_form.rating.data))
    print(review_form.body.data)
    if review_form.validate():
        rating = review_form.rating.data
        body = review_form.body.data
        user_id = current_user.id
        review = Review(rating=rating, body=body, game_id=game_id, user_id=user_id)
        db.session.add(review)
        db.session.commit()
        return redirect(url_for('get_game', game_id=game_id))
    return redirect(url_for('get_game', game_id=game_id))


@app.route('/search')
def search():
    name = request.args.get('title', '')
    games = Game.query.filter(Game.title.like(f'%{name}%')).all()
    return render_template('index.html', title="Nintendon't", games=games)


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@app.template_filter('date_format')
def date_format(value, format='%x'):
    return value.strftime(format)


if __name__ == '__main__':
    app.run()
