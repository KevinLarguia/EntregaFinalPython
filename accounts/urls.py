from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.register_view, name='register'),
    path('perfil/', views.ProfileView.as_view(), name='profile'),
    path('perfil/editar/', views.profile_update_view, name='edit_profile'),
    path('perfil/cambiar-password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
]
