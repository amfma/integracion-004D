from app import db
from models import EspacioComun, Reserva, Residente, Unidad, Deuda, Condominio, Pagos
import datetime
import mailer
from math import floor
from datetime import date
from dateutil.relativedelta import relativedelta

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

def get_residentes_unidad(unidad_id):
    residentes = Residente.query.filter_by(unidad_id=unidad_id, estado_id=1).all()
    return residentes

def get_unidad(id):
    unidad = Unidad.query.filter_by(id=id).first()
    return unidad

def get_unidades_condominio(condominio_id):
    unidades = Unidad.query.filter_by(condominio_id=condominio_id).all()
    return unidades

def get_deudas(unidad_id):
    deudas = Deuda.query.filter_by(unidad_id=unidad_id, pagado='N').all()
    return deudas

def post_deuda(concepto, monto, fecha_emision, fecha_vencimiento, tipo_deuda_id, unidad_id):
    deuda = Deuda(
        concepto = concepto,
        monto = monto,
        fecha_emision = fecha_emision,
        fecha_vencimiento = fecha_vencimiento,
        tipo_deuda_id = tipo_deuda_id,
        unidad_id = unidad_id,
        pagado = "N"
    )
    db.session.add(deuda)
    db.session.commit()
    return deuda.id

def prorratear(condominio_id, monto):
    unidades = get_unidades_condominio(condominio_id) 
    for unidad in unidades:
        alicuota = unidad.alicuota
        today = date.today()
        monto_deuda = floor(monto * (alicuota/100))
        # ingresa la nueva deuda
        post_deuda(
            monto = monto_deuda,
            fecha_emision = str(today),
            fecha_vencimiento = str(today + relativedelta(months=1)),
            concepto = 'Gasto Común',
            tipo_deuda_id = 1,
            unidad_id = unidad.id,
        )
        # Envía correo a los usuarios
        residentes = get_residentes_unidad(unidad.id)
        for residente in residentes:
            usuario = residente.nombres + ' ' + residente.apellidos
            mailer.cuenta_total(usuario=usuario, valor=monto_deuda, mail=residente.correo)
    return unidades

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

def crear_pago(rut, monto, token):
    residente = Residente.query.filter_by(rut=rut).first()
    unidad_id = residente.unidad_id
    pago = Pagos(
        monto = monto,
        token = token,
        residente_rut = rut,
        unidad_id = unidad_id,
        fecha = datetime.datetime.now(),
        estado_pago_id = 1
    )
    db.session.add(pago)
    db.session.commit()