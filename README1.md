# Aplicación completa de back y front end

A pesar de que esta aplicación es completa, aún no se tiene la conexión a la base de datos, puesto que resulta una aplicación tan sencilla que no hace falta. Para correr esta aplicación es importante tener activos ambos servidores, esto se logra con
los comandos mostrados a continuación, ambos se deben de ejecutar en terminales por separado para que se tengan ambos procesos corriendo al mismo tiempo. (Asumiendo que ya se haya copiado esta rama)

## Ejecución del back-end

Para iniciar el servidor back-end, basta con ejecutar los siguientes comandos:

`cd http-producer`
`python -m flask run`

Si por alguna razón no está instalado alguna dependencia entonces primero se tiene que ejecutar el siguiente comando:

`pip install -r requirements.txt`

Si al final aparece la url <a>http://127.0.0.1:5000/</a> entonces el servidor back-end está listo para recibir peticiones (ya sea de Postman o del servidor front-end)

## Ejecución del front-end

Para levantar el front end basta con hacer los siguientes comandos:

`cd ConexionBackFront`
`npm start`

Y después de aproximadamente 15 minutos, debería de aparecer una ventana del navegador predeterminado con la vista de la aplicación, que con el back-end listo, debería de poder funcionar de manera correcta. Si por alguna razón llega a fallar esta aplicación de React, entonces hay que ejecutar un `npm install` o `npm i` para mayor simplicidad.
