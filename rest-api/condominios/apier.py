from app import db
from models import EspacioComun, Reserva

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
    reserva = Reserva.query.filter_by(id=id).first()
    return reserva

def put_reserva(id, fecha):
    reserva = Reserva.query.filter_by(id=id).first()
    reserva.fecha = fecha
    db.session.commit()