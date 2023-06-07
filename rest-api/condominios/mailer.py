import yagmail
direccion_remitente = 'miscondominios7@gmail.com'
password = 'umjcmreupjoxxrdf'

def cuenta_total(usuario, valor, mail):
    texto_correo = f'Estimado/a {usuario}: Le informaos que usted tiene una deuda pendiente por un total de ${valor}'
    correo = yagmail.SMTP(direccion_remitente, password=password)
    correo.send(subject='Deuda pendiente', to=mail, contents=texto_correo)

def pagado(usuario, total, mail):
    texto_correo = f'Estimado/a {usuario}: Le informaos que usted ha pagado una deuda por ${total}'
    correo = yagmail.SMTP(direccion_remitente, password=password)
    correo.send(subject='Pago Deuda', to=mail, contents=texto_correo)

pagado('Andrés', 20, 'an.mpodozis@duocuc.cl')