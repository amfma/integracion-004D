insert into condominio (direccion, nombre) values ('Av. pajaritos', 'Los pajaros');
insert into horario (descripcion) values ('AM');
insert into horario (descripcion) values ('PM');
insert into estado (descripcion) values ('Activo');
insert into estado (descripcion) values ('Anulado');
insert into unidad (descripcion, condominio_id) values ('A14', 1);
insert into tipo_espacio (nombre) values ('Piscina');
insert into tipo_espacio (nombre) values ('Quincho');
insert into tipo_espacio (nombre) values ('Sala de Eventos');
insert into espacio_comun (descripcion, condominio_id, tipo_espacio_id) values ('Piscina', 1, 1);
insert into espacio_comun (descripcion, condominio_id, tipo_espacio_id) values ('Quincho', 1, 2);
insert into espacio_comun (descripcion, condominio_id, tipo_espacio_id) values ('Sala de Eventos', 1, 3);
insert into residente (rut, nombres, apellidos, propietario, telefono, correo, contrasena, estado_id, unidad_id) values ('11111111-1', 'Arturo', 'Gomez', '0', 999999999, 'agomez@test.com', 'password123', 1, 1);
insert into reserva (fecha, pagado, horario_id, espacio_comun_id, estado_id, residente_rut) values ('2023-05-13', '0', 1, 1, 1, '11111111-1');
insert into tipo_deuda (descripcion) values ('Gasto Común');
insert into tipo_deuda (descripcion) values ('Multa');
insert into deuda (concepto, monto, pagado, fecha_emision, fecha_vencimiento, tipo_deuda_id, unidad_id) 
    values ('Gastos comunes Mayo', 100000, 'N', '2023-06-01', '2023-06-30', '1', '1');
insert into deuda (concepto, monto, pagado, fecha_emision, fecha_vencimiento, tipo_deuda_id, unidad_id) 
    values ('Multa ruidos molestos', 30000, 'N', '2023-06-01', '2023-07-30', '2', '1');