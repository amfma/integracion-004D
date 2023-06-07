from app import db
from models import EspacioComun, Reserva, Residente, Unidad, Deuda, Condominio

def get_espacios():
    espacios = EspacioComun.query.all()
    return espacios

def get_reservas():
    reservas = Reserva.query.filter_by(estado_id=1).all()
    return reservas

def post_reserva(fecha, rut, pagado=0, horario_id=1, espacio_comun_id=1, estado_id=1):
    reserva = Reserva(
        fecha = fecha,
        pagado = pagado,
        horario_id = horario_id,
        espacio_comun_id = espacio_comun_id,
        estado_id = estado_id,
        residente_rut = rut
    )
    db.session.add(reserva)
    db.session.commit()
    return reserva.id

def del_reserva(id):
    reserva = Reserva.query.filter_by(id=id).first()
    reserva.estado_id = 2
    db.session.commit()

def get_reserva(id):
    reserva = Reserva.query.filter_by(id=id, estado_id=1).first()
    return reserva

def put_reserva(id, fecha):
    reserva = Reserva.query.filter_by(id=id).first()
    reserva.fecha = fecha
    db.session.commit()

def get_espacios_condominio(condominio_id):
    espacios = EspacioComun.query.filter_by(condominio_id=condominio_id).all()
    return espacios

def get_reservas_espacio(espacio_comun_id):
    reservas = Reserva.query.filter_by(espacio_comun_id=espacio_comun_id, estado_id=1).all()
    return reservas

def get_residente(rut):
    residente = Residente.query.filter_by(rut=rut, estado_id=1).first()
    return residente

def get_unidad(id):
    unidad = Unidad.query.filter_by(id=id).first()
    return unidad

def get_deudas(unidad_id):
    deudas = Deuda.query.filter_by(unidad_id=unidad_id, pagado='N').all()
    return deudas

def get_condominios():
    condominios = Condominio.query.all()
    return condominios

def get_valor_deuda(deuda_id):
    deuda = Deuda.query.filter_by(id=deuda_id).first()
    return deuda.monto

def pagar_deuda(deuda_id):
    deuda = Deuda.query.filter_by(id=deuda_id).first()
    deuda.pagado = 'P'
    db.session.commit()