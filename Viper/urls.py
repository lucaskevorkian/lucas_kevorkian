from django.urls import path
from . import views




urlpatterns = [
    path('index', views.index, name='index'),
    path("motor", views.motor, name= "motor"),
    path("precio", views.precio, name= "precio"),
    path("buscar_auto", views.buscar_auto, name= "buscar_auto"),
]
