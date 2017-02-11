from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/postgres'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    print('hey')
