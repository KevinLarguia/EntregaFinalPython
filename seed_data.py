"""
Script para crear datos de prueba. Ejecutar con:
    python manage.py shell < seed_data.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')
django.setup()

from django.contrib.auth.models import User
from pages.models import Page
from accounts.models import UserProfile

# Crear superusuario admin si no existe
if not User.objects.filter(username='admin').exists():
    admin = User.objects.create_superuser(
        username='admin',
        email='admin@blog.com',
        password='admin1234',
        first_name='Adrian',
        last_name='García',
    )
    print(f'Superusuario creado: admin / admin1234')
else:
    admin = User.objects.get(username='admin')
    print('Superusuario admin ya existe')

# Crear usuario de prueba si no existe
if not User.objects.filter(username='testuser').exists():
    user2 = User.objects.create_user(
        username='testuser',
        email='test@blog.com',
        password='test1234',
        first_name='Juan',
        last_name='Pérez',
    )
    print('Usuario de prueba creado: testuser / test1234')
else:
    user2 = User.objects.get(username='testuser')
    print('testuser ya existe')

# Crear perfiles si no existen (los signals deberían haberlos creado)
for user in [admin, user2]:
    profile, created = UserProfile.objects.get_or_create(user=user)
    if created:
        profile.bio = f'Hola, soy {user.first_name} y me encanta escribir sobre tecnología y viajes.'
        profile.save()
        print(f'Perfil creado para {user.username}')

# Crear blogs de prueba
blogs = [
    {
        'title': 'Introducción a Python: El lenguaje del futuro',
        'subtitle': 'Por qué Python es el lenguaje más popular del mundo',
        'content': '''<h2>¿Por qué aprender Python?</h2>
<p>Python es uno de los lenguajes de programación más versátiles y populares del mundo. Su sintaxis clara y legible lo hace ideal tanto para principiantes como para desarrolladores experimentados.</p>
<h3>Ventajas principales</h3>
<ul>
    <li><strong>Sintaxis limpia:</strong> El código en Python es fácil de leer y escribir.</li>
    <li><strong>Gran comunidad:</strong> Miles de librerías disponibles en PyPI.</li>
    <li><strong>Versatilidad:</strong> Desde web hasta inteligencia artificial.</li>
    <li><strong>Alta demanda laboral:</strong> Las empresas buscan desarrolladores Python.</li>
</ul>
<p>Si todavía no empezaste a aprender Python, ¡este es el momento perfecto!</p>''',
        'author': admin,
    },
    {
        'title': 'Django: El framework web de Python por excelencia',
        'subtitle': 'Cómo construir aplicaciones web robustas en tiempo récord',
        'content': '''<h2>¿Qué es Django?</h2>
<p>Django es un framework web de alto nivel escrito en Python que fomenta el desarrollo rápido y el diseño limpio y pragmático. Fue creado en 2005 y desde entonces se ha convertido en uno de los frameworks más populares del mundo.</p>
<h3>Características destacadas</h3>
<ul>
    <li><strong>ORM potente:</strong> Manejo de base de datos sin escribir SQL.</li>
    <li><strong>Admin automático:</strong> Panel de administración listo para usar.</li>
    <li><strong>Seguridad:</strong> Protección contra CSRF, XSS, inyección SQL.</li>
    <li><strong>Escalabilidad:</strong> Usado por Instagram, Pinterest y Disqus.</li>
</ul>
<blockquote><p>"The web framework for perfectionists with deadlines."</p></blockquote>
<p>En este blog iremos cubriendo todos los aspectos de Django desde cero hasta nivel avanzado.</p>''',
        'author': admin,
    },
    {
        'title': 'Bases de datos relacionales con SQLite',
        'subtitle': 'Todo lo que necesitás saber sobre SQLite en tus proyectos Django',
        'content': '''<h2>SQLite: simple y poderoso</h2>
<p>SQLite es el motor de base de datos por defecto en Django para desarrollo. Es liviano, no requiere servidor y funciona perfecto para proyectos pequeños y medianos.</p>
<h3>¿Cuándo usar SQLite?</h3>
<p>SQLite es ideal cuando:</p>
<ul>
    <li>Estás desarrollando o haciendo pruebas locales.</li>
    <li>Tu aplicación tiene pocos usuarios concurrentes.</li>
    <li>Querés algo simple sin configuración extra.</li>
</ul>
<h3>¿Cuándo migrar a PostgreSQL?</h3>
<p>Cuando tu app crezca y necesites alta concurrencia, es momento de migrar a PostgreSQL. Django hace esta transición muy sencilla gracias a su ORM.</p>''',
        'author': user2,
    },
    {
        'title': 'CSS y Bootstrap: diseño responsive sin complicaciones',
        'subtitle': 'Cómo crear interfaces modernas con Bootstrap 5',
        'content': '''<h2>Bootstrap 5 al rescate</h2>
<p>Bootstrap es el framework CSS más popular del mundo. Con su sistema de grillas y componentes pre-diseñados, podés crear interfaces profesionales en minutos.</p>
<h3>Lo mejor de Bootstrap 5</h3>
<ul>
    <li>Sin dependencia de jQuery.</li>
    <li>Sistema de grillas de 12 columnas.</li>
    <li>Componentes: navbar, cards, modals, forms.</li>
    <li>Utilidades de espaciado, colores y tipografía.</li>
</ul>
<p>En este proyecto usamos Bootstrap 5 integrado con Django templates para tener un diseño limpio y responsive desde el primer día.</p>''',
        'author': user2,
    },
    {
        'title': 'Autenticación en Django: Login, Logout y Registro',
        'subtitle': 'Implementando un sistema de usuarios completo paso a paso',
        'content': '''<h2>Sistema de autenticación en Django</h2>
<p>Django viene con un sistema de autenticación robusto que maneja usuarios, grupos y permisos. En este artículo veremos cómo implementar login, logout y registro de usuarios.</p>
<h3>Vistas clave</h3>
<ul>
    <li><strong>LoginView:</strong> Vista basada en clase para el inicio de sesión.</li>
    <li><strong>LogoutView:</strong> Vista para cerrar sesión.</li>
    <li><strong>CreateView:</strong> Para el registro de nuevos usuarios.</li>
</ul>
<h3>Proteger vistas</h3>
<p>Usamos <code>@login_required</code> como decorador y <code>LoginRequiredMixin</code> en CBVs para proteger las vistas que requieren autenticación.</p>
<p>¡El sistema está completamente funcionando en este blog!</p>''',
        'author': admin,
    },
]

created_count = 0
for blog_data in blogs:
    if not Page.objects.filter(title=blog_data['title']).exists():
        Page.objects.create(**blog_data)
        created_count += 1
        print(f'Blog creado: "{blog_data["title"]}"')
    else:
        print(f'Ya existe: "{blog_data["title"]}"')

print(f'\n=== Seed completado ===')
print(f'Blogs creados: {created_count}')
print(f'Total blogs en DB: {Page.objects.count()}')
print(f'\nCredenciales:')
print(f'  Admin:    admin / admin1234  -> /admin/')
print(f'  Usuario:  testuser / test1234')
