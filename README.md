# Pasos para crear la base de datos y ejecutar el proyecto

## PASO 1 — Crear la base de datos MSQL en Docker

```bash
# Crear contenedor MySQL con base 'subscripcion'
docker run -d --name mi_mysql \
    -e MYSQL_ROOT_PASSWORD=1234 \
    -e MYSQL_DATABASE=subscripcion \
    -p 3306:3306 \
    mysql:8.0

# Entrar al contenedor
docker exec -it mi_mysql bash

# Conectarse a MySQL
mysql -u root -p 1234

# Crear tabla
CREATE TABLE users (
    username VARCHAR(255),
    lastname VARCHAR(255),
    correo VARCHAR(100),
    cel VARCHAR(10),
    horario_llamada VARCHAR(50)
);
```
# PASOS PARA BAJR UN REPOSITORIO

## Pasos para ejecutar el proyecto
```git
# git https://github.com/CAAG842/Carlos_Aquino_2022100571 EF_CARLOS_AQUINO_2022100571
# git remote remove origin (desvincular del repositorio GitHub)
# CORRER EL APP.PY EN VISUAL ESTUDIO CODE
