from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.InboxView.as_view(), name='inbox'),
    path('enviados/', views.SentView.as_view(), name='sent'),
    path('nuevo/', views.compose_view, name='compose'),
    path('nuevo/<int:receiver_id>/', views.compose_view, name='compose_to'),
    path('<int:pk>/', views.message_detail_view, name='detail'),
]
