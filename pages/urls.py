from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.PageListView.as_view(), name='list'),
    path('crear/', views.PageCreateView.as_view(), name='create'),
    path('<int:pk>/', views.PageDetailView.as_view(), name='detail'),
    path('<int:pk>/editar/', views.PageUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', views.page_delete, name='delete'),
]
