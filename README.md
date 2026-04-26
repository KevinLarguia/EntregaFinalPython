# Mi Blog - Entrega Final Módulo Python

Aplicación web de blog desarrollada con Python y Django como proyecto final de la Diplomatura en Python.

## Tecnologías utilizadas

- Python 3.x
- Django 4.2
- Bootstrap 5
- SQLite
- CKEditor (editor de texto enriquecido)
- Pillow (manejo de imágenes)

## Funcionalidades

- **Home**: Página principal con las últimas publicaciones
- **Acerca de mí**: Información sobre el autor del blog (`/about/`)
- **Páginas (Blog)**: Listado y detalle de páginas con búsqueda (`/pages/`)
- **CRUD de páginas**: Crear, editar y eliminar páginas (requiere login)
- **Autenticación**: Registro, login y logout de usuarios
- **Perfil de usuario**: Ver y editar perfil, cambiar contraseña
- **Mensajería**: Sistema de mensajes entre usuarios registrados
- **Admin**: Panel de administración Django para todos los modelos

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd EntregaFinalModuloPython
```

### 2. Crear y activar entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (administrador)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

### 7. Abrir en el navegador

- Sitio web: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Estructura del proyecto

```
EntregaFinalModuloPython/
├── myblog/             # Configuración del proyecto Django
├── pages/              # App principal (blog)
├── accounts/           # App de autenticación y perfiles
├── messaging/          # App de mensajería
├── templates/          # Templates HTML
├── static/             # Archivos estáticos (CSS, JS, imágenes)
├── manage.py
└── requirements.txt
```

## Requisitos implementados

- [x] Herencia de templates con base.html y NavBar
- [x] Vista Home, About (`/about/`), Pages (`/pages/`)
- [x] Modelo `Page` con 2 CharField, RichTextField (CKEditor), ImageField, DateField
- [x] CRUD completo de páginas con login requerido para editar/eliminar
- [x] Búsqueda de páginas con mensaje de "no hay resultados"
- [x] App `accounts` con login, logout y registro (username, email, password)
- [x] Perfil de usuario con avatar, bio, fecha de nacimiento
- [x] Edición de perfil y cambio de contraseña
- [x] App `messaging` con bandeja de entrada, mensajes enviados y redacción
- [x] Mínimo 2 CBVs (`PageListView`, `PageDetailView`, `PageCreateView`, `InboxView`, etc.)
- [x] Mínimo 1 mixin en CBV (`LoginRequiredMixin` en `PageCreateView`, `ProfileView`, etc.)
- [x] Mínimo 1 decorador en FBV (`@login_required` en `page_delete`, `profile_update_view`, etc.)
- [x] Todos los modelos registrados en el admin
- [x] `.gitignore` con `__pycache__`, `db.sqlite3` y `media`

## Autor

Proyecto final del Módulo de Python - Diplomatura en Python
