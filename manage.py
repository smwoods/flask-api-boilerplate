#!/usr/bin/env python
import os
from flask_script import Manager

from app.app import app, db

manager = Manager(app)

@manager.command
def runserver():
    db.create_all()
    app.run()

if __name__ == "__main__":
    manager.run()
