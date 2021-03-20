from flask import Flask, render_template, request, abort, redirect, url_for
from models import db, Game, User
from flask_migrate import Migrate
from forms import LoginForm, RegisterForm
from flask_login import login_user, logout_user, LoginManager

app = Flask(__name__)
app.secret_key = 'v{O#GgvaO@Rp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db.init_app(app)
migrate = Migrate(app, db)
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


@app.route('/games/new')
def create_game():
    return render_template('new_game.html')


@app.route('/games/<int:game_id>')
def get_game(game_id):
    game = Game.query.filter_by(id=game_id).first_or_404()
    return render_template('game.html', game=game)


@app.route('/search')
def search():
    name = request.args.get('title', '')
    games = Game.query.filter(Game.title.like(f'%{name}%')).all()
    return render_template('index.html', title="Nintendon't", games=games)


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run()
