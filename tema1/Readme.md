PASO 1 CREAR BASE DE DATOS
docker run -d --name mi_mysql -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=subscripcion -p 3306:3306 mysql:8.0

docker exec -it mi_mysql bash

mysql -u root -p 1234

CREATE TABLE users (
 username VARCHAR(255),
lastname VARCHAR(255),
correo VARCHAR(100),
cel VARCHAR(10),
horario_llamada VARCHAR(50));

Paso 2 
Abrir en visual estudio el tema 2 
y correr el app.py
