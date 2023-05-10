from flask import Flask, jsonify, make_response, redirect, request
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from os import environ
import apier

app = Flask(__name__)
app.debug = True

# conexion a MYSQL
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(['DATABASE_URI'])
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy()

from models import *
with app.app_context():
    db.init_app(app)
    db.create_all()
migrate = Migrate(app, db)

@app.route('/admin/espacios', methods = ['GET'])
def list_espacios():
    headers = {"Content-Type": "application/json"}
    espacios = apier.get_espacios()
    return make_response(jsonify(espacios), 200, headers)

@app.route('/admin/reservas', methods = ['GET', 'POST'])
def api_reservas():
    if request.method == 'GET':
        headers = {"Content-Type": "application/json"}
        reservas = apier.get_reservas()
        return make_response( jsonify(reservas), 200, headers)
    if request.method == 'POST':
        headers = {"Content-Type": "application/json"}
        data = request.get_json()
        reserva = apier.post_reserva(fecha=data['fecha'], rut=data['rut'])
        return make_response('Exitoso', 200, headers)
    
@app.route('/admin/reservas/del/<int:id>', methods=['DELETE'])
def del_reservas(id):
    reserva = id
    apier.del_reserva(id)
    return redirect('/admin/reservas')

@app.route('/admin/reservas/<int:id>', methods=['GET','PUT'])
def api_reserva(id):
    if request.method == 'GET':
        reserva = apier.get_reserva(id)
        headers = {"Content-Type": "application/json"}
        return make_response(jsonify(reserva), 200, headers)
    if request.method == 'PUT':
        reserva = id
        data = request.get_json()
        reserva = apier.put_reserva(id, fecha=data['fecha'])

if __name__ == '__main__':
    app.run(debug=True)

