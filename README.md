# Pasos para crear la base de datos y ejecutar el proyecto

## PASO 1 — Crear la base de datos MySQL en Docker

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
# PASOS PARA BAJAR UN REPOSITORIO

## Pasos para ejecutar el proyecto
```git
# git clone https://github.com/gusmanulop/repasoPPI.git EF_GUSTAVO_LOPEZ
# git remote remove origin (desvincular del repositorio GitHub)
# git remote add origin https/TuPropioRepositorio.git
# git add .
# git commit -m "mensaje editable
# git push -u origin master
