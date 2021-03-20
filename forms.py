from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import Email, DataRequired, EqualTo
from wtforms.widgets import PasswordInput


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
