from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login #es para poder usar el nombre login y darle 2 argumentos
from .forms import formulario_creacion_usuario, formulario_edicion_perfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import DatosExtra



def login(request):
    formulario = AuthenticationForm()

    if request.method == "POST":   #va por que es un form que va por post
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            # nombre_usuario = formulario.cleaned_data.get("username")
            # contra = formulario.cleaned_data.get("password")        
            # usuario = authenticate(username = nombre_usuario, password = contra)
            
            usuario = formulario.get_user()
            
            django_login(request, usuario)
            
            DatosExtra.objects.get_or_create(user=usuario)
            
            return redirect("inicio")
    
    return render(request, "usuarios/login.html" , {"form": formulario})


def register(request):
    
    formulario = formulario_creacion_usuario()
    
    if request.method == "POST":    
        formulario = formulario_creacion_usuario(request.POST)
        if formulario.is_valid():
            formulario.save()
              
            return redirect("usuarios:login")
    
    return render(request, "usuarios/register.html", {"form": formulario})


@login_required
def editar_perfil(request):
    datos_extra = request.user.datosextra
    formulario = formulario_edicion_perfil(instance=request.user, initial={"avatar": datos_extra.avatar, "fecha_nacimiento": datos_extra.fecha_nacimiento})
    
    if request.method == "POST":
        formulario = formulario_edicion_perfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            new_avatar = formulario.cleaned_data.get("avatar")
            new_nacimiento = formulario.cleaned_data.get("fecha_nacimiento")
 
            datos_extra.avatar = new_avatar if new_avatar else datos_extra.avatar
            datos_extra.fecha_nacimiento = new_nacimiento if new_nacimiento else datos_extra.fecha_nacimiento
            datos_extra.save()
            formulario.save()
              
            return redirect("inicio")
    return render(request, "usuarios/editar_perfil.html", {"form": formulario})

class cambiar_password(LoginRequiredMixin, PasswordChangeView):
    template_name = "usuarios/cambiar_password.html"
    success_url = reverse_lazy("usuarios:editar_perfil")