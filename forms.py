from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField
from wtforms.validators import Email, DataRequired, EqualTo
from wtforms.widgets import PasswordInput, TextArea


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = StringField(label='Пароль', widget=PasswordInput(), validators=[DataRequired()])
    remember_me = BooleanField(label='Запомнить меня')


class RegisterForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    first_name = StringField(label='Имя', validators=[DataRequired()])
    last_name = StringField(label='Фамилия', validators=[DataRequired()])
    password = StringField(label='Пароль', widget=PasswordInput(), validators=[DataRequired()])
    confirmation = StringField(label='Подтверждение пароля', widget=PasswordInput(), validators=[DataRequired(), EqualTo('password')])


class ReviewForm(FlaskForm):
    rating = RadioField(label='Оценка', choices=[
        (5, 'Отлично'),
        (4, 'Хорошо'),
        (3, 'Нормально'),
        (2, 'Плохо'),
        (1, 'Ужасно'),
    ], validators=[DataRequired()])
    body = StringField(label='Комментарий', widget=TextArea(), validators=[DataRequired()])
