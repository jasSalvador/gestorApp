# GestorAPP 📝

En función de mi proyecto personal previamente establecido - App web para comunidades, juntas de vecinos o cursos que necesiten organizar integrantes, cuotas, dineros recaudados o eventos - he implementado las diferentes tecnologías y competencias técnicas adquiridas en el modulo 3: **Fundamentos de programación en Python**.

Como **primera etapa**: 'Fundamentos de programación en Python', he desarrollado un menú principal que permite acceder a las diferentes secciones del proyecto: **cuotas, integrantes y gastos** cada una con su propio menú para ver, crear, editar, eliminar. Por el momento, el funcionamiento es a través de la terminal.

**Segunda etapa**: 'Programación avanzada en python'. El proyecto ahora está realizado bajo el paradigma de progrmación orientada a objetos (POO), con clases para representar las entidades principales (Integrantes, Cuotas y Gastos) y un gestor principal (Gestorprincipal) que organiza la lógica del sistema. He mantenido y actualizado el menú principal para adaptarlo a esta nueva versión con POO. 

**Tercera etapa**: 'Desarrollo de aplicaciones web con Python y Django'. He migrado todo el proyecto a Django, cree una app "gestor" donde he implementado los modelos, rutas, vistas y templates, integrando base de datos SQLite3. Además he implementado formularios de registro para administradores e integrantes, con login y vistas protegidas.

**Cuarta etapa**: 'Acceso a datos en aplicaciones Pyhton y Django'. En esta etapa he migrado de SQLite a MySQL, cree un nuevo superusuario y he implementado funciones como mostrar listado de cuotas pagadas, editar datos personales y eliminar elementos, completando asi, crud completo, también mejoré la seguridad agregando validaciones a las vistas y funcionalidades exclusivas para administradores.

## Integración de Django con bases de datos 📂
Django se integra con distintos motores de bases de datos (SQLite, Postgres, MySQL). En este proyecto se comenzó con
SQLite para luego migrar a MySQL. La conexión se configura en `settings.py` indicando motor, nombre de la base de datos, usuario y contraseña. Django gestiona automaticamente las conexiones y operaciones, lo que permite trabajar con objetos Python, en lugar de SQL directo.

## Aplicaciones preinstaladas de Django 💥
Este proyecto utiliza varias aplicaciones que vienen con Django:
- **django.contrib.admin**: panel administrativo para gestionar modelos
- **django.contrib.auth**: sistema de autenticación y permisos
- **django.contrib.sessions**: manejo de sesiones de usuarios
- **django.contrib.messages**: para manejo de mensajes
Estas aplicaciones permiten acelerar el desarrollo y asegurar funcionalidades básicas sin necesidad de implementarlo desde cero.

## Modelos 💫
- **Integrante**: persona que pertenece a una organización, con datos personales y relación a cuotas.
- **Organización**: representa la comunidad o grupo que usa la aplicación y centraliza, integrantes, cuotas y gastos.
- **Cuota**: pago realizado por un integrante, asociado a mes, año y organización.
- **Gasto**: registro de un gasto de la organización, con nombre, fecha, total y sus items asociados.
- **ItemGasto**: detalle específico dentro de un gasto, con nombre y monto, vinculado al gasto correspondiente.

- **Modelos sin relaciones**: se implementaron entidades simples como Organización y Cuota, que en su primera versión no tenian relaciones entre si.

- **Modelos con relaciones**: se implementaron relaciones uno a muchos y muchos a muchos:
- `Integrante` con `Organizacion` (ForeingKey)
- `Cuota` con `Integrante` (ForeingKey)
- `Gasto` con `ItemGasto` (ForeingKey con related_name='items')
- Estas relaciones permiten modelar escenario reales de gestión de cuotas y gastos.

## Funcionalidades actuales 🚀

### Integrantes
- Registro personal desde formulario web 
- Asociación según organización a la que pertenece
- Ver sus cuotas pagadas
- Ver todos los gastos de la organización a la que pertenece
**Nuevas funcionalides**:
- Editar datos personales
- Eliminar cuenta

### Administradores
- Registro personal desde formulario web
- Creación de organización a la que representan
- Agregar pagos de cuotas
- Agregar gastos con sus respectivos items
- Ver listado completo de integrantes en tabla
- Ver todos los gastos de la organización
**Nuevas funcionalidades**:
- Ver listado con todas las cuotas pagadas
- Eliminar integrante
- Eliminar pago de cuota
- Eliminar gasto

### Cuotas
- Administradores pueden registrar pago de cuota por integrante desde formulario
- Se muestran cuotas pagadas según integrante
**Nuevas funcionalidades**:
- Se muestra listado de todas las cuotas pagadas

### Gastos
- Registrar gastos por actividad (ej: fiesta, reparación) desde formulario
- Agregar múltiples items dentro de un gasto (ej: bebidas, decoración) desde formulario
- Se muestran todos los gastos y su detalle

## Templates 🎇
El proyecto incluye templates en Django para:
- Login y registro
- Registrar, listar y visualizar cuotas
- Registrar, listar y visualizar gastos y detalles de gastos
- Registrar items de gastos
**Nuevos templates**:
- Listado de cuotas pagadas
- Confirmación de eliminación para integrante - cuota - gasto

## Administración 🔑
- Se creó un superusuario para acceder al panel de administración de Django
- Solo el superusuario tiene acceso al panel de admin de Django
- Todos los modelos están registrados en el admin

## Futuras mejoras planeadas 🎯
- Se agregó validación para funciones y vistas exclusivas para administradores ✅
- Editar datos personales ✅
- Eliminar cuenta ✅
- Eliminar gasto ✅
- Eliminar cuota ✅
- Integración a POO ✅
- Migración completa a Django ✅
- Integración con base de datos ✅

## Ejecución 📌
1. Clonar el repositorio
2. Crear y activar entorno virtual: 
    - Windows: `python -m venv venv` -> `.\venv\Scripts\activate`
    - Linux/Mac: `python3 -m venv venv` -> `sourse venv/bin/activate`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Crear la base de datos en MySQL con el nombre: `gestorapp_django`
5. Configurar creedenciales en `settings.py`
6. Ejecutar migraciones: `python manage.py makemigrations` `python manage.py migrate`
7. Crear superusuario: `python manage.py createsuperuser`
8. Ejecutar el servidor: `python manage.py runserver`
9. Acceder a: `http://localhost:8000`

## Uso GestorApp 🎊
- **Login y registro**: 
- Todas las vistas requieren login
- El acceso se hace primero por `/login` o `/registro`
- Una vez dentro, el usuario es redirigido a `inicio`

-**Flujo general**
1. En `home` selecciona registrarte como admin y crea tu cuenta como admin de una organización (también quedaras registrado como integrante de dicha organización)
2. Una vez exista una organización, se pueden registrar integrantes para dicha organización
3. Accede a `login` e inicia sesión

-**Flujo de administrador**:
- En `inicio` están todos los acceso a todas las funcionalidades de la app:
- Crear una organización al registrarse
- Ver listado de todos los integrantes con opción para eliminar
- Ver listado de todas las cuotas pagadas con opción para eliminar
- Registrar pago de cuota
- Registrar una actividad y luego agregar items de gastos asociados
- Ver todos los gastos de la organización con acceso a detalles y eliminación de gasto
- En detalle de gasto opción para agregar más items de gasto
- Ver todas tus cuotas pagadas
- Editar cuenta
- Eliminar cuenta

-**Flujo integrantes**:
- Registrarse en la organización correspondiente
- Ver todos los gastos de la organización con acceso a detalles
- Ver todas tus cuotas pagadas
- Editar cuenta
- Eliminar cuenta

-**Panel de administración de Django**:
- Acceder a /admin/ con el superusuario
- Gestionar directamente los modelos (Integrante - Organizacion - Cuota - Gasto - ItemGasto)

## Autora 👩🏻‍💻

Jasmin S | Fan del código bonito ✨