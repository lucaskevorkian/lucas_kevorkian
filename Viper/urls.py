from django.urls import path
from . import views
from .views import crear_avion, buscar_avion, ver_avion, borrar_avion




urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path("sobre_mi", views.sobre_mi, name= "sobre_mi"), 
    path("buscar_auto", views.buscar_auto, name= "buscar_auto"),
    path("crear_auto", views.crear_auto, name= "crear_auto"),
    path("ver_auto/<int:id>", views.ver_auto, name= "ver_auto"),
    path("borrar_auto/<int:id>", views.borrar_auto, name= "borrar_auto"),
    path("editar_auto/<int:id>", views.editar_auto, name= "editar_auto"),
    
    path('avion/crear/', crear_avion.as_view(), name='crear_avion'),
    path('avion/<int:pk>/', ver_avion.as_view(), name='ver_avion'),
    path('avion/<int:pk>/editar/', crear_avion.as_view(), name='editar_avion'),
    path('avion/', buscar_avion.as_view(), name='buscar_avion'),
    path('avion/<int:id>/borrar/', borrar_avion, name='borrar_avion'),

    

]
