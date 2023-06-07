from flask import Flask, jsonify, make_response, redirect, request
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from os import environ
import apier, transbanky, mailer

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
        reserva = apier.post_reserva(
            fecha=data['fecha'], 
            rut=data['rut'], 
            pagado=data['pagado'],
            horario_id=data['horario_id'],
            espacio_comun_id=data['espacio_comun_id'],
            )
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

@app.route('/admin/condominios', methods=['GET'])
def api_condominios():
    headers = {"Content-Type": "application/json"}
    condominios = apier.get_condominios()
    return make_response(jsonify(condominios), 200, headers)

@app.route('/admin/gastos_comunes', methods=['POST'])
def api_gastos_comunes():
    headers = {"Content-Type": "application/json"}
    data = request.get_json()
    try:
        prorratear = apier.prorratear(data['condominio_id'], data['monto'])
        if prorratear != []:
            return make_response('Exitoso', 200, headers)
        else: 
            return make_response('Condomino no existe', 200, headers)
    except:
       respuesta = {'Error': 'Error no especificado'}
       return make_response(jsonify(respuesta), 400, headers)
    
@app.route('/residente/espacios/<int:condominio_id>', methods = ['GET'])
def list_espacios_condiminio(condominio_id):
    headers = {"Content-Type": "application/json"}
    espacios = apier.get_espacios_condominio(condominio_id)
    return make_response(jsonify(espacios), 200, headers)

@app.route('/residente/reservas/<int:espacio_comun_id>', methods = ['GET'])
def list_reservas_espacio(espacio_comun_id):
    headers = {"Content-Type": "application/json"}
    reservas = apier.get_reservas_espacio(espacio_comun_id)
    return make_response(jsonify(reservas), 200, headers)

@app.route('/residente/residente/<string:rut>', methods=['GET'])
def api_residente(rut):
    headers = {"Content-Type": "application/json"}
    residente = apier.get_residente(rut)
    return make_response(jsonify(residente), 200, headers)

@app.route('/residente/unidad/<int:id>', methods=['GET'])
def api_unidad(id):
    headers = {"Content-Type": "application/json"}
    unidad = apier.get_unidad(id)
    return make_response(jsonify(unidad), 200, headers)

@app.route('/residente/reservar', methods=['POST'])
def api_reserva_res():
    headers = {"Content-Type": "application/json"}
    data = request.get_json()
    reserva = apier.post_reserva(
        fecha = data['fecha'],
        rut= data['rut'],
        horario_id= data['horario_id'],
        espacio_comun_id= data['espacio_comun_id']
    )
    return make_response('Exitoso', 200, headers)

@app.route('/residente/deudas/<int:id>', methods=['GET'])
def get_deudas(id):
    headers = {"Content-Type": "application/json"}
    deudas = apier.get_deudas(unidad_id=id)
    return make_response(jsonify(deudas), 200, headers)

@app.route('/residente/pago', methods=['POST'])
def pagar():
    headers = {"Content-Type": "application/json"}
    data = request.get_json()
    ### EL SIGUIENTE BLOQUE ES SOLO PARA INTEGRAR EL MAIL, DE SER NECESARIO
    #try:
     #   residente = apier.get_residente(rut=data['rut'])
    #except:
     #   residente = apier.get_residente(rut='1111111111')
    ####
    deudas = data['deudas']
    total = 0
    for x in deudas:
        total += apier.get_valor_deuda(x)
    try:
        respuesta = transbanky.nueva_transaccion(total)
        for x in deudas:
            apier.pagar_deuda(x)
        # apier.crear_pago(monto=total, rut=data['rut'], token=respuesta['token'])
        # mailer.pagado(residente.nombre, total, residente.correo)
        mailer.pagado('Andrés Mpodozis', total=total, mail='am.mpodozis@duocuc.cl')
        return make_response(jsonify(respuesta), 200, headers)
    except:
        respuesta = {'Error': 'Error con transbank'}
        return make_response(jsonify(respuesta), 500, headers)
        

@app.route('/residente/confirma_pago/<string:token>', methods=['GET'])
def verificar(token):
    headers = {"Content-Type": "application/json"}
    try:
        respuesta = transbanky.confirmar_transaccion(token=token)
        if respuesta['vci'] == "TSY":
            return make_response(jsonify(respuesta), 200, headers)
        else:
            return make_response(jsonify(respuesta), 400, headers)
    except:
        respuesta = {'Error': 'Error no especificado'}
        return make_response(jsonify(respuesta), 400, headers)


if __name__ == '__main__':
    app.run(debug=True)