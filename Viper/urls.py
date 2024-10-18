from django.urls import path
from . import views




urlpatterns = [
    path('index', views.index, name='index'),
    path("sobre_mi", views.sobre_mi, name= "sobre_mi"),
    path("precio", views.precio, name= "precio"),
    path("buscar_auto", views.buscar_auto, name= "buscar_auto"),
    path("crear_auto", views.crear_auto, name= "crear_auto"),
    
]
