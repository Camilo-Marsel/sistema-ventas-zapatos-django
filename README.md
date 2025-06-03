# Sistema de Gestión de Ventas con Django 🛒

Este es un sistema web para la gestión de ventas, inventario y reportes, desarrollado con Django. Soporta múltiples roles de usuario (Administrador, Vendedor) y permite llevar un control sobre los productos vendidos, existencia en bodega, y estadísticas.

## 🚀 Características principales

- Gestión de zapatos (CRUD)
- Gestión de ventas con control de stock
- Reportes diarios de ventas
- Control de roles (admin, vendedor)
- Sistema de autenticación (login/logout)
- Interfaz adaptable por tipo de usuario
- Panel de administración de Django habilitado

## ⚙️ Instalación

1. Clona el repositorio:

bash: 
git https://github.com/Camilo-Marsel/sistema-ventas-zapatos-django.git
cd sistema-ventas-zapatos-django```

2. Crea un entorno virtual y actívalo:

python -m venv env
env\Scripts\activate  # En Windows

3. Instala dependencias:

pip install -r requirements.txt

4. Ejecuta migraciones:

python manage.py migrate

5. Crea un superusuario:

python manage.py createsuperuser

6. Inicia el servidor:

python manage.py runserver


## Usuarios y roles

## Administrador: 
Puede gestionar inventario, ventas y usuarios.

## Vendedor: 
Solo puede registrar ventas.

## Inventario:
Encargado de cambios en el stock de invetario.