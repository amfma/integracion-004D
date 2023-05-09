from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from os import environ

app = Flask(__name__)
app.debug = True

# conexion a MYSQL
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy()

from models import *
with app.app_context():
    db.init_app(app)
    db.create_all()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()