# Repositorio de AWS Lambda para procesamiento de pagos en MercadoPago

**Este repositorio contiene una funci贸n de AWS Lambda para procesar pagos en MercadoPago utilizando la SDK de MercadoPago.
Funcionamiento**
___
**馃挕IMPORTANTE:鈿狅笍 _El link del endpoint lambda podria dejar de funcionar, porque no tuve facilidades para tener mi propia cuenta aws por problemas de tarjeta. Es por ello que me prest茅 la cuenta de un gran amigo mio, asi que para prevenir riesgo de no generar gastos en aws, eliminar茅 pronto los servicios de lambda, es por ello que mas adelante en apartado de pruebas muestro el correcto funcionamiento_**
_(Tambien el profesor Jose Lozano ya me revis贸)_

La funci贸n toma un evento y un contexto como par谩metros y utiliza el m贸dulo json para cargar los datos del pago en formato JSON desde el cuerpo del evento. Los datos se almacenan en una variable y se env铆an a la SDK de MercadoPago para crear el pago. La respuesta del pago se almacena en una variable y se devuelve en el cuerpo de la respuesta de la funci贸n con un c贸digo de estado 200.
Dependencias

    json
    os
    mercadopago

## Configuraci贸n

Antes de utilizar la funci贸n, debe agregar su token de prueba de MercadoPago como una variable de entorno en el entorno de ejecuci贸n de AWS Lambda.
Uso
_Para utilizar esta funci贸n, simplemente env铆e una solicitud POST con los datos de pago en formato JSON en el cuerpo de la solicitud. Aseg煤rese de incluir todos los campos necesarios para crear un pago en MercadoPago._

## Prueba de funcionamiento
### Imagen de envio desde postman
![Captura de pantalla de Grabaci贸n de pantalla desde 2023-01-14 00-32-23 webm](https://user-images.githubusercontent.com/26263355/212807982-a1d713b1-3023-4427-8bd7-c33c267c942a.png)

### Imagen de cloudwatch
__se oberva 00:32 la misma hora que envie request en postman
![imagen](https://user-images.githubusercontent.com/26263355/212808511-2a558b54-2be0-46b0-9723-5ca39a929f16.png)

### Video de funcionamiento de carrito de compra
[grabacion-de-pantalla-desde-2023-01-16-23-29-27_7PRH1yW6.webm](https://user-images.githubusercontent.com/26263355/212812215-4dbb0f38-2321-4355-a64d-c1af3babc346.webm)


## Nota

Este repositorio y su contenido se proporcionan "tal cual" y sin garant铆a de ning煤n tipo, ya sea expresa o impl铆cita. Utilice bajo su propio riesgo.

## Contribuciones
Este repositorio est谩 abierto a contribuciones de la comunidad. Si desea contribuir, por favor env铆e una solicitud de pull con sus cambios. Aseg煤rese
de seguir nuestras gu铆as de estilo y de documentar adecuadamente sus cambios. Si encuentra alg煤n error o tiene sugerencias para mejorar la funci贸n, por favor abra un issue para discutirlo.
