from datetime import datetime, timedelta
from app import db, login
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from time import time


class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(40), index=True)
    last_name = db.Column(db.String(40))
    password = db.Column(db.String(128))
    email_confirmed = db.Column(db.DateTime, default=None)
    date_joined = db.Column(db.DateTime, default=datetime.utcnow)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def set_password(self, p):
        self.password = generate_password_hash(p)

    def verify_password(self, p):
        return check_password_hash(self.password, p)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {"reset_password": self.id, "exp": time() + expires_in},
            current_app.config["SECRET_KEY"],
            algorithm="HS256",
        ).decode("utf-8")

    def get_confirm_email_token(self, expires_in=3600):
        return jwt.encode(
            {"confirm_email": self.id, "exp": time() + expires_in},
            current_app.config["SECRET_KEY"],
            algorithm="HS256",
        ).decode("utf-8")

    @staticmethod
    def verify_reset_password_token(token):
        try:
            pk = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )["reset_password"]
        except:
            return None
        return User.query.get(pk)

    @staticmethod
    def verify_confirm_email_token(token):
        try:
            pk = jwt.decode(
                token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
            )["confirm_email"]
        except:
            return None
        return User.query.get(pk)

    def __repr__(self):
        return f"<User: {self.id}>"


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class School(db.Model):

    __tablename__ = "school"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), index=True)
    tipo = db.Column(db.String(40))
    telefone = db.Column(db.String(12))
    email = db.Column(db.String(60))
    logradouro = db.Column(db.String(120))
    bairro = db.Column(db.String(50))
    cidade = db.Column(db.String(70))
    uf = db.Column(db.String(10))
    cep = db.Column(db.String(9))
    created_in = db.Column(db.DateTime, default=datetime.utcnow)
