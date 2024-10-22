from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login #es para poder usar el nombre login y darle 2 argumentos
from .forms import formulario_creacion_usuario
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