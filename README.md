
# Sistema de Inventario Simple con Flask

Este es un proyecto de un sistema de inventario simple desarrollado con Flask, que permite la gestión de productos y la autenticación de usuarios.

## Tabla de Contenidos

- [Características](#características)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Rutas](#rutas)

## Características

- Registro de nuevos usuarios.
- Inicio de sesión y cierre de sesión.
- Creación, lectura, actualización y eliminación (CRUD) de productos.
- Interfaz sencilla basada en HTML.

## Tecnologías Utilizadas

- [Flask](https://flask.palletsprojects.com/) - Framework web para Python.
- [Werkzeug](https://werkzeug.palletsprojects.com/) - Utilidades para el manejo de contraseñas.
- [SQLite](https://www.sqlite.org/) - Base de datos ligera.

## Requisitos Previos

Asegúrate de tener instalados los siguientes programas:

- Python 3.7 o superior.
- pip (gestor de paquetes de Python).

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecuta la aplicación:**
   ```bash
   flask run
   ```

4. **Accede a la aplicacion:**
   ```bash
   http://127.0.0.1:5000/
   ```

## Uso

- Registrar un nuevo usuario: Accede a la ruta /register y completa el formulario para crear un nuevo usuario.
- Iniciar sesión: Usa la ruta /login para iniciar sesión con tus credenciales.
- Gestionar productos: Una vez que inicies sesión, podrás ver el inventario y realizar operaciones CRUD en los productos.

## Rutas

- GET / - Página principal del inventario.
- POST /product - Crear un nuevo producto.
- GET /product/<id> - Obtener detalles de un producto.
- PUT /product/<id> - Actualizar un producto existente.
- DELETE /product/<id> - Eliminar un producto.
- GET /login - Página de inicio de sesión.
- POST /login - Procesar el inicio de sesión.
- GET /register - Página de registro de usuario.
- POST /register - Procesar el registro de un nuevo usuario.
- GET /logout - Cerrar sesión.

