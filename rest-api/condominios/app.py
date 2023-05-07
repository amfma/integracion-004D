from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from os import environ

app = Flask(__name__)
app.debug = True

# conexion a MYSQL
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')

db = SQLAlchemy(app)
with app.app_context():
    db.create_all()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()