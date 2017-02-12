from uuid import uuid4
import bcrypt

from app.app import db

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.Binary(60))

    def __init__(self, username, password):
        self.id = str(uuid4())
        self.username = username
        self.password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())

    def verify_password(self, password):
        return bcrypt.checkpw(str.encode(str(password)), self.password)

    def __repr__(self):
        return '<User %r>' % self.username
