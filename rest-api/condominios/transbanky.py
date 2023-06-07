import random
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions, IntegrationCommerceCodes, IntegrationApiKeys
from transbank.common.integration_type import IntegrationType

#Orden de compra para usar en las pruebas
ORDEN = str(random.randrange(1000000, 99999999))
URL = 'http://localhost:8081/confirmacion_pago'
SESION = str(random.randrange(1000000, 99999999))

def nueva_transaccion(monto):
    tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))
    respuesta = tx.create(buy_order=ORDEN, session_id=SESION, amount=monto, return_url=URL)
    return {'url': respuesta['url'], 'token': respuesta['token']}

def confirmar_transaccion(token):
    tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY, IntegrationType.TEST))
    respuesta = tx.commit(token=token)
    data = {
        'vci' : respuesta['vci'],
        'response_status': respuesta['response_code'],
        'amount': respuesta['amount'],
        'buy_order': respuesta['buy_order']
    }
    return data