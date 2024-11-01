 
from django.urls import path
from . import views
app_name = "chat"
urlpatterns = [
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('ver/', views.ver_mensajes, name='ver_mensajes'), 
    path('<str:room_name>/', views.room, name='room'),
]
