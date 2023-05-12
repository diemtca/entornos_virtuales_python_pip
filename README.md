# Game Project
Proceso adecuado para que cualquier persona pueda ejecutar el proyecto

sh: significa lenguaje en terminal

Para correr el juego debes seguir las siguientes instrucciones en la terminal


```sh
cd game
python3 game.py
```

# Entornos virtuales

Para crear entornos virtuales debes y asignar paquetes especificos a dicho entorno debes:

```sh
#instala el paquete para crear entornos virtuales
sudo apt install -y python3-venv 
#crea el ambiente virtual
python3 -m venv <nombre_del_ambiente_virtual>
#activa el ambiente virtual
source <nombre_del_ambiente_virtual>/bin/activate
# deactivate #comando para desactivar el v_env
pip3 freeze #muestra los packg instalados
pip3 install <paquete>
pip3 install <paquete>==<version_especifica_del_paquete>
```
Ahora bien, existe una manera de automatizar el proceso guardando los paquetes que deben instalarse en un archivo .txt que llamaremos requirements.txt

```sh
#asigna todo los paquetes instalados al archivo 
pip3 freeze > requirements.txt
#visualizamos el contenido del archivo para verificar
cat requirements.txt
#instalamos todos los pkgs que contenga requirements.txt
pip3 install -r requirements.txt
```

# App Project


```sh
#clonar el proyecto a tu computadora
git clone
cd app
#crea el ambiente virtual
python3 -m venv env
#activar en ambiente virtual
source env/bin/activate
#instalar los pksg o dependencias
pip3 install -r requirements.txt

python3 main.py
```
# App Project with docker

Utilizamos docker para aislar completamente las apps de python, en este caso SCRIPTS: en versiones de python, en este lenguaje de programación sin importar que sistema operativo quiera correr el proyecto sin siquiera instalar python en la computadora local, y asi correr cualquier lenguaje en el contenedor

```sh
#clonar el proyecto a tu computadora
git clone
cd app
#construir el contenedor con docker
docker-compose build
# lanzar el contenedor
docker-compose up -d
#verificamos el estado del contenedor
docker-compose ps
#ingresamos al contenedor
docker-compose exec app-csv bash
```
Puedes ir al localhost:8000 y ver correr el web-server 
localhost:8000
localhost:8000/contact
localhost:8000/contactHtml
# Web-server lo que necesitas saber

Crear un servidor web

Fastapi es la libreria de python que usamos para construir el servidor web

Uvicorn es un servidor que nos ayuda a lanzar en linea el servidor que construimos
```sh
#instalar las fastapi de python
pip3 install fastapi
pip3 instal "uvircorn[standard]"
#añade los paquetes en el requirements.txt
pip3 freeze >requirements.txt

```
# Web-server Project


```sh
#clonar el proyecto a tu computadora
git clone
cd web-server
#crea el ambiente virtual
python3 -m venv env
#activar en ambiente virtual
source env/bin/activate
#instalar los pksg o dependencias
pip3 install -r requirements.txt

uvircorn main:app --reload
```
# Web-server Project

Utilizamos docker para crear un contenedor para correr un servicio (servidor web) que se va mantener al aire y desplegarlo facilmente a la nube

```sh
#clonar el proyecto a tu computadora
git clone
cd web-server
#construir el contenedor con docker
docker-compose build
# lanzar el contenedor
docker-compose up -d
#verificamos el estado del contenedor
docker-compose ps
```
Puedes ir al localhost:8080 y ver correr el web-server en un contenedor

localhost:8080
localhost:8080/contact
localhost:8080/contactHtml

Dockerizamos una aplicación web, la cual esta muy cerca de ser lanzada a desarrollo

Sigue aprendiendo!