from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField, IntegerField, DateField
from wtforms.validators import Email, DataRequired, EqualTo, URL
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


class GameForm(FlaskForm):
    title = StringField(label='Название', validators=[DataRequired()])
    desc = StringField(label='Описание', validators=[DataRequired()], widget=TextArea())
    poster = StringField(label='Обложка', validators=[DataRequired(), URL()], description='Используйте обложки с соотношением 2:1.')
    price = IntegerField(label='Цена', validators=[DataRequired()])
    release_date = DateField(label='Дата релиза', validators=[DataRequired()])
    on_sale = BooleanField(label='Распродажа')


class ReviewForm(FlaskForm):
    rating = RadioField(label='Оценка', choices=[
        (5, 'Отлично'),
        (4, 'Хорошо'),
        (3, 'Нормально'),
        (2, 'Плохо'),
        (1, 'Ужасно'),
    ], validators=[DataRequired()])
    body = StringField(label='Комментарий', widget=TextArea(), validators=[DataRequired()])
