from datetime import date
from app import db
from dataclasses import dataclass

Base = db.Model


class Administrador(Base):

    __tablename__ = 'administrador'

    rut = db.Column(db.String(10), primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.Integer(), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    contrasena = db.Column(db.String(32), nullable=False)
    condominio_id = db.Column(db.Integer(), db.ForeignKey('condominio.id'), nullable=False)


class Condominio(Base):

    __tablename__ = 'condominio'

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    direccion = db.Column(db.String(100), nullable=False)
    nombre = db.Column(db.String(50))


class Conserje(Base):

    __tablename__ = 'conserje'

    rut = db.Column(db.String(10), primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.Integer(), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    contrasena = db.Column(db.String(32), nullable=False)
    condominio_id = db.Column(db.Integer(), db.ForeignKey('condominio.id'), nullable=False)


class Directivo(Base):

    __tablename__ = 'directivo'

    rut = db.Column(db.String(10), primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.Integer(), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    contrasena = db.Column(db.String(32), nullable=False)
    condominio_id = db.Column(db.Integer(), db.ForeignKey('condominio.id'), nullable=False)

@dataclass
class EspacioComun(Base):

    __tablename__ = 'espacio_comun'

    id:int = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    descripcion:str = db.Column(db.String(50), nullable=False)
    monto:int = db.Column(db.Integer())
    condominio_id:int = db.Column(db.Integer(), db.ForeignKey('condominio.id'), nullable=False)
    tipo_espacio_id:int = db.Column(db.Integer(), db.ForeignKey('tipo_espacio.id'), nullable=False)


class Estado(Base):

    __tablename__ = 'estado'

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    descripcion = db.Column(db.String(20), nullable=False)

@dataclass
class Deuda(Base):
    
    __tablename__ = 'deuda'

    id:int = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    concepto:str = db.Column(db.String(100), nullable=False)
    monto:int = db.Column(db.Integer(), nullable=False)
    pagado:str = db.Column(db.String(1), nullable=False) #P:pendiente, S:si, N:no
    fecha_emision:date = db.Column(db.TIMESTAMP(), nullable=False)
    fecha_vencimiento:date = db.Column(db.TIMESTAMP(), nullable=False)
    tipo_deuda_id:int = db.Column(db.Integer(), db.ForeignKey('tipo_deuda.id'), nullable=False) # multa o gasto comun
    unidad_id:int = db.Column(db.Integer(), db.ForeignKey('unidad.id'), nullable=False)

class TipoDeuda(Base):

    __tablename__ = 'tipo_deuda'

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    descripcion = db.Column(db.String(20), nullable=False)

#DEPRECADA
@dataclass
class GastoComun(Base):

    __tablename__ = 'gasto_comun'

    id:int = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    monto:int = db.Column(db.Integer(), nullable=False)
    pagado:str = db.Column(db.String(1), nullable=False)
    unidad_id:int = db.Column(db.Integer(), db.ForeignKey('unidad.id'), nullable=False)


class Horario(Base):

    __tablename__ = 'horario'

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    descripcion = db.Column(db.String(10), nullable=False)

#DEPRECADA
@dataclass
class Multa(Base):

    __tablename__ = 'multa'

    id:int = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    monto:int = db.Column(db.Integer(), nullable=False)
    concepto:str = db.Column(db.String(100), nullable=False)
    pagado:str = db.Column(db.String(1), nullable=False)
    unidad_id:int = db.Column(db.Integer(), db.ForeignKey('unidad.id'), nullable=False)


class Pagos(Base):

    __tablename__ = 'pagos'

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    monto = db.Column(db.Integer(), nullable=False)
    concepto = db.Column(db.String(100), nullable=False)
    residente_rut = db.Column(db.String(10), db.ForeignKey('residente.rut'), nullable=False)
    unidad_id = db.Column(db.Integer(), db.ForeignKey('unidad.id'), nullable=False)

@dataclass
class Reserva(Base):

    __tablename__ = 'reserva'

    id:int = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    fecha:date = db.Column(db.TIMESTAMP(), nullable=False)
    pagado:str = db.Column(db.String(1))
    horario_id:int = db.Column(db.Integer(), db.ForeignKey('horario.id'), nullable=False)
    espacio_comun_id:int = db.Column(db.Integer(), db.ForeignKey('espacio_comun.id'), nullable=False)
    estado_id:int = db.Column(db.Integer(), db.ForeignKey('estado.id'), nullable=False)
    residente_rut:str = db.Column(db.String(10), db.ForeignKey('residente.rut'), nullable=False)

@dataclass
class Residente(Base):

    __tablename__ = 'residente'

    rut:str = db.Column(db.String(10), primary_key=True)
    nombres:str = db.Column(db.String(100), nullable=False)
    apellidos:str = db.Column(db.String(100), nullable=False)
    propietario:str= db.Column(db.String(1), nullable=False)
    telefono:int = db.Column(db.Integer(), nullable=False)
    correo:str = db.Column(db.String(100), nullable=False)
    contrasena:str = db.Column(db.String(32), nullable=False)
    estado_id:int = db.Column(db.Integer(), db.ForeignKey('estado.id'), nullable=False)
    unidad_id:int = db.Column(db.Integer(), db.ForeignKey('unidad.id'), nullable=False)


class TipoEspacio(Base):

    __tablename__ = 'tipo_espacio'

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)

@dataclass
class Unidad(Base):

    __tablename__ = 'unidad'

    id:int = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    descripcion:str = db.Column(db.String(10), nullable=False)
    condominio_id:int = db.Column(db.Integer(), db.ForeignKey('condominio.id'), nullable=False)