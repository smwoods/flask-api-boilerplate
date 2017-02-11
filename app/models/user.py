from rally.app import db
from uuid import uuid4

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.id = str(uuid4())
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
