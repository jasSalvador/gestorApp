# GestorAPP

En función de mi proyecto personal previamente establecido - App web para comunidades, juntas de vecinos o cursos que necesiten organizar integrantes, cuotas, dineros recaudados o eventos - he implementado las diferentes tecnologías y competencias técnicas adquiridas en el modulo 3: **Fundamentos de programación en Python**.

Como **primera etapa**: 'Fundamentos de programación en Python', he desarrollado un menú principal que permite acceder a las diferentes secciones del proyecto: **cuotas, integrantes y gastos** cada una con su propio menú para ver, crear, editar, eliminar. Por el momento, el funcionamiento es a través de la terminal.

**Segunda etapa**: 'Programación avanzada en python'. El proyecto ahora está realizado bajo el paradigma de progrmación orientada a objetos (POO), con clases para representar las entidades principales (Integrantes, Cuotas y Gastos) y un gestor principal (Gestorprincipal) que organiza la lógica del sistema. He mantenido y actualizado el menú principal para adaptarlo a esta nueva versión con POO. 

**Tercera etapa**: 'Desarrollo de aplicaciones web con Python y Django'. He migrado todo el proyecto a Django, cree una app "gestor" donde he implementado los modelos, rutas, vistas y templates, integrando base de datos SQLite3. Además he implementado formularios de registro para administradores e integrantes, con login y vistas protegidas.

## Modelos 💫
**Integrante**: persona que pertenece a una organización, con datos personales y relación a cuotas.
**Organización**: representa la comunidad o grupo que usa la aplicación y centraliza, integrantes, cuotas y gastos.
**Cuota**: pago realizado por un integrante, asociado a mes, año y organización.
**Gasto**: registro de un gasto de la organización, con nombre, fecha, total y sus items asociados.
**ItemGasto**: detalle específico dentro de un gasto, con nombre y monto, vinculado al gasto correspondiente.

## Funcionalidades actuales 🚀

### Integrantes
- Registro personal desde formulario web 
- Asociación según organización a la que pertenece
- Ver sus cuotas pagadas
- Ver todos los gastos de la organización a la que pertenece

### Administradores
- Registro personal desde formulario web
- Creación de organización a la que representan
- Agregar pagos de cuotas
- Agregar gastos con sus respectivos items
- Ver listado completo de integrantes en tabla
- Ver todos los gastos de la organización

### Cuotas
- Administradores pueden registrar pago de cuota por integrante desde formulario
- Se muestran cuotas pagadas según integrante

### Gastos
- Registrar gastos por actividad (ej: fiesta, reparación) desde formulario
- Agregar múltiples items dentro de un gasto (ej: bebidas, decoración) desde formulario
- Se muestran todos los gastos y su detalle

## Templates 🎇
El proyecto incluye templates en Django para:
- Login y registro
- Registrar y visualizar cuotas
- Registrar, listar y visualizar detalles de gastos
- Registrar items de gastos

## Administración 🔑
- Se creó un superusuario para acceder al panel de administración de Django
- Todos los modelos están registrados en el admin

## Futuras mejoras planeadas 🎯
- Editar datos personales
- Eliminar cuenta
- Eliminar gasto
- Eliminar cuota
- Integración a POO ✅
- Migración completa a Django ✅
- Integración con base de datos ✅

## Ejecución 📌
1. Clonar el repositorio
2. Crear y activar entorno virtual: python -m venv venv .\venv\Scripts\activate
3. Instalar dependencias: pip install -r requirements.txt
4. Ejecutar migraciones: python manage.py migrate
5. Crear superusuario: python manage.py createsuperuser
6. Ejecutar el servidor: python manage.py runserver
7. Acceder a: http://localhost:8000


## Autora 👩🏻‍💻

Jasmin S | Fan del código bonito ✨