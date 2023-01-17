import json
import os
import mercadopago

def lambda_handler(event, context):
    # Inicializar una instancia del SDK de MercadoPago utilizando el token de prueba almacenado en las variables de entorno de mi lambda
    # Agregue en una capa nueva mi python.zip que contiene el paquete mercadopago
    sdk = mercadopago.SDK(os.environ["TEST_TOKEN"])
    # Carga los datos enviados en el cuerpo del evento en formato json y almacena en requestdata
    requestData = json.loads(event["body"])
    # Crear un diccionario con los datos necesarios para crear un pago en MercadoPago, tomando los valores del diccionario requestData
    payment_data = {
        "transaction_amount": float(requestData["transaction_amount"]),
        "token": requestData["token"],
        "installments": int(requestData["installments"]),
        "payment_method_id": requestData["payment_method_id"],
        "issuer_id": requestData["issuer_id"],
        "payer": {
            "email": requestData["payer"]["email"],
            "identification": {
                "type": requestData["payer"]["identification"]["type"], 
                "number": requestData["payer"]["identification"]["number"]
            }
        }
    }
    # Utiliza el SDK de MercadoPago para crear un pago con los datos especificados en el diccionario payment_data
    payment_response = sdk.payment().create(payment_data)
    # Almacenar la respuesta del pago en my variable myres
    myres = payment_response["response"]
    # duevuelve un objeto json con el código de estado 200 y el cuerpo de la respuesta del pago en formato json
    return {
        "statusCode": 200,
        "body": json.dumps(myres)
    }
