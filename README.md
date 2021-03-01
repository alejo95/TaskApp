# API_TaskApp

Rest Api de creación de tareas, desarrollada en Django Rest Framework bajo el patron MVT en este proyecto se encuentra una REST API la cual se conecta a una base de datos Sqli3 ( Base De datos relacional )

## Comenzando 🚀

Prerequisitos para poder correr el proyecto, recordemos que este proyecto esta en django por ende es necesario tener como base Python3 instalado, a continuación se dan unas recomendaciones para correr el proyecto


### Pre-requisitos 📋

Para correr este proyecto se recomida crear un entorno virtual y dentro de este correr el comando el archivo requirements.txt Que viene dentro de la carpeta raíz del el proyecto, esto lo puedes hacer con el comando

```
$ brew install python3
```

### Instalación 🔧

Para correr este proyecto se recomienda crear un entorno virtual y dentro de este correr el comando el archivo requirements.txt Que viene dentro de la carpeta raíz del el proyecto, esto lo puedes hacer con el comando

```
$ pip install -r requirements.txt
```

Una instalados los requerimientos de nuestro archivo requerimientos.txt, procedemos a crear las migraciones con los comandos 

```
$ python manage.py makemigrations
$ python manage.py migrate
```

Una vez realizado esto procedemos a correr el servidor

```
$ python manage.py runserver
```



## Ejecutando las pruebas ⚙️

Durante el proceso de creación se utilizaron dos tipos de prubas, unas manuales por medios de http con los metodos Post, Put, Get, Delete

### Pruebas con Postman 🔩

Estas pruebas se podran ver con sus respectivos ejemplos en la url siguiente
Postman

[Postman](https://web.postman.co/workspace/My-Workspace~ac55a5b7-a91a-4b88-8627-e5ed30813c1e/documentation/7262894-01cc7241-ff01-46eb-b5d9-dc05e29591f9) - PostMan web 

### Ejecucion test Unitarios 🔩

Para ejecutar los test unitarios tenemos que ejecutar principalmente el servido con el comando

```
$ python manage.py runserver
```

Una vez ejecutado el servidor ejecutamos, procedemos a ejecutar los test unitarios con el comando

```
$ python manage.py test apps
```



## Construido con 🛠️

* [Django](https://www.djangoproject.com) - Framework
* [Django Rest Framework](https://www.django-rest-framework.org) - Framework
* [SQLite](https://www.sqlite.org/index.html) - Base de datos

## Diagramas

Diagramas de base de datos relacional v_001

 ![img](https://cdn.discordapp.com/attachments/804077015916347402/813867756050317332/Screen_Shot_2021-02-23_at_3.19.46_PM.png)



# Diagrama de vistas (basda en componentes)

Se generaron 3 componentes (apps) las cuales están compuestas por lo siguiente:

- contiene las bases de las estructuras, esto con el fin de optimizar código (implementado paradigma de herencia), como las estructuras de los serializadores (con las estructuras que se repiten fácilmente)
- Users: contiene la lógica de los usuarios CRUD
- Task: Dentro de task se encuentra la lógica de creación de las tareas junto con los modulos que compone la lógica de unificación de las vistas

![img](https://cdn.discordapp.com/attachments/482617495254073344/813844681385312307/Screen_Shot_2021-02-23_at_1.47.53_PM.png)



## Proceso y generacion de tareas

Para el proceso de creación de tareas se utilizó la metodología Kanban con el fin de listar las diferentes tareas a realizar para lograr el producto final 

![img](https://cdn.discordapp.com/attachments/804077015916347402/813867237927813120/Screen_Shot_2021-02-23_at_3.17.41_PM.png)

---

