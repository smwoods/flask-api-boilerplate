#!/usr/bin/env python
from flask_script import Manager

from rally.app import app, db
from rally.models import User


manager = Manager(app)

@manager.command
def runserver():
    db.create_all()
    app.run()

if __name__ == "__main__":
    manager.run()
