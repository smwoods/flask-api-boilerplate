import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT

app = Flask(__name__)
app.config.from_object('app.config')
db = SQLAlchemy(app)

from .models.user import User
def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.verify_password(password):
        return user

def identify(payload):
    user_id = payload['identity']
    return User.query.get(user_id)

jwt = JWT(app, authenticate, identify)

from .routes.user import user_blueprint
app.register_blueprint(user_blueprint, url_prefix='/user')
