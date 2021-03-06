from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    first_name = db.Column(db.String(32), nullable=False)
    is_admin = db.Column(db.Boolean, server_default='0')
