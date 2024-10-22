from django.shortcuts import render, redirect
from .models import Auto, Avion
from .forms import crear_auto_formulario, buscar_auto_formulario, config_basica
from django.views.generic.edit import CreateView, UpdateView 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(request):
    return render(request, 'inicio.html')


def sobre_mi(request):
    return render(request, "sobre_mi.html")
 
def buscar_auto(request):
    formulario = buscar_auto_formulario(request.GET)
    if formulario.is_valid():
        marca = formulario.cleaned_data.get("Marca")
        modelo = formulario.cleaned_data.get("Modelo")
        año = formulario.cleaned_data.get("Año")
        precio = formulario.cleaned_data.get("Precio")
        hp= formulario.cleaned_data.get("Hp")
        
        filtros = {}
        if marca:
            filtros['marca__icontains'] = marca  
        if modelo:
            filtros['modelo__icontains'] = modelo  
        if año is not None:  
            filtros['año'] = año
        if precio is not None:  
            filtros['precio'] = precio
        if hp is not None:  
            filtros['hp'] = hp
        autos = Auto.objects.filter(**filtros)  # Descomponemos el diccionario en clave=valor
    return render(request, "buscar_auto.html", {"autos": autos, "form": formulario})


@login_required
def crear_auto(request):
    formulario = crear_auto_formulario()
    if request.method == "POST":
        formulario = crear_auto_formulario(request.POST)
        if formulario.is_valid():  
            data = formulario.cleaned_data
            auto = Auto(marca=data.get("Marca"), modelo=data.get("Modelo"), año=data.get("Año"), precio=data.get("Precio"), hp=data.get("Hp"))
            auto.save()
            return redirect("buscar_auto")
             
        return render(request, "crear_auto.html", {"form": formulario})
    return render(request, "crear_auto.html", {"form": formulario})
    
    
def ver_auto(request, id):
    auto = Auto.objects.get(id=id)
    return render(request, "ver_auto.html", {"auto": auto})
    

@login_required  
def borrar_auto(request, id):
    auto = Auto.objects.get(id=id)
    auto.delete()
    return redirect("buscar_auto")


@login_required
def editar_auto(request, id):
    auto = Auto.objects.get(id=id)
    form = config_basica(initial={"Marca":auto.marca, "Modelo":auto.modelo, "Año":auto.año, "Precio":auto.precio, "Hp":auto.hp}) #sirve para get
    
    if request.method == "POST":
        form = config_basica(request.POST)  #sirve para post
        if form.is_valid():
            auto.marca = form.cleaned_data.get("marca")
            auto.modelo = form.cleaned_data.get("modelo")
            auto.año = form.cleaned_data.get("año")
            auto.precio = form.cleaned_data.get("Precio")
            auto.hp= form.cleaned_data.get("Hp") 
        auto.save
            
        return redirect("buscar_auto")
    return render(request, "editar_auto.html", {"form": form, "auto": auto})
     


class crear_avion(LoginRequiredMixin, CreateView):
    model = Avion
    template_name = "crear_avion.html"
    success_url = reverse_lazy("buscar_avion")
    fields = ["modelo", "año", "altitud"]

class buscar_avion(ListView):
    model = Avion
    template_name = "buscar_avion.html"
    context_object_name = "aviones"
    
class ver_avion(DetailView):
    model = Avion
    template_name='ver_avion.html'

    

class editar_avion(LoginRequiredMixin, UpdateView): 
    model = Avion
    template_name='editar_avion.html'
    success_url = reverse_lazy("buscar_avion")
    fields = ["modelo", "año", "altitud"]


@login_required  
def borrar_avion(request, id):
    avion = Avion.objects.get(id=id)
    avion.delete()
    return redirect("buscar_avion")
