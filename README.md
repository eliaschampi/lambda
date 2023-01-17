# Repositorio de AWS Lambda para procesamiento de pagos en MercadoPago

**Este repositorio contiene una función de AWS Lambda para procesar pagos en MercadoPago utilizando la SDK de MercadoPago.
Funcionamiento**
___
**💡IMPORTANTE:⚠️ _El link del endpoint lambda podria dejar de funcionar, porque no tuve facilidades para tener mi propia cuenta aws por problemas de tarjeta. Es por ello que me presté la cuenta de un gran amigo mio, asi que para prevenir riesgo de no generar gastos en aws, eliminaré pronto los servicios de lambda, es por ello que mas adelante en apartado de pruebas muestro el correcto funcionamiento_**
_(Tambien el profesor Jose Lozano ya me revisó)_

La función toma un evento y un contexto como parámetros y utiliza el módulo json para cargar los datos del pago en formato JSON desde el cuerpo del evento. Los datos se almacenan en una variable y se envían a la SDK de MercadoPago para crear el pago. La respuesta del pago se almacena en una variable y se devuelve en el cuerpo de la respuesta de la función con un código de estado 200.
Dependencias

    json
    os
    mercadopago

## Configuración

Antes de utilizar la función, debe agregar su token de prueba de MercadoPago como una variable de entorno en el entorno de ejecución de AWS Lambda.
Uso
_Para utilizar esta función, simplemente envíe una solicitud POST con los datos de pago en formato JSON en el cuerpo de la solicitud. Asegúrese de incluir todos los campos necesarios para crear un pago en MercadoPago._

## Prueba de funcionamiento
### Imagen de envio desde postman
![Captura de pantalla de Grabación de pantalla desde 2023-01-14 00-32-23 webm](https://user-images.githubusercontent.com/26263355/212807982-a1d713b1-3023-4427-8bd7-c33c267c942a.png)

### Imagen de cloudwatch
__se oberva 00:32 la misma hora que envie request en postman
![imagen](https://user-images.githubusercontent.com/26263355/212808511-2a558b54-2be0-46b0-9723-5ca39a929f16.png)

### Video de funcionamiento de carrito de compra
[grabacion-de-pantalla-desde-2023-01-16-23-29-27_7PRH1yW6.webm](https://user-images.githubusercontent.com/26263355/212812215-4dbb0f38-2321-4355-a64d-c1af3babc346.webm)


## Nota

Este repositorio y su contenido se proporcionan "tal cual" y sin garantía de ningún tipo, ya sea expresa o implícita. Utilice bajo su propio riesgo.

## Contribuciones
Este repositorio está abierto a contribuciones de la comunidad. Si desea contribuir, por favor envíe una solicitud de pull con sus cambios. Asegúrese
de seguir nuestras guías de estilo y de documentar adecuadamente sus cambios. Si encuentra algún error o tiene sugerencias para mejorar la función, por favor abra un issue para discutirlo.
