from django.shortcuts import render, redirect, get_object_or_404
from .models import Auto, Avion
from .forms import crear_auto_formulario, buscar_auto_formulario, config_basica, editar_auto_form, AvionForm
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

def editar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)  # Pasa el modelo Auto como primer argumento
    
    # Usa el formulario correcto; parece que config_basica no es el formulario que deseas.
    formulario = editar_auto_form(instance=auto)  # Si editar_auto_form es tu formulario correcto para esta vista

    if request.method == "POST":
        formulario = editar_auto_form(request.POST, request.FILES, instance=auto)  # Pasa 'auto' como instancia
        if formulario.is_valid():
            auto.foto = formulario.cleaned_data.get('foto') or auto.foto  # Mantiene la foto existente si no se sube una nueva
            auto.foto_url = formulario.cleaned_data.get('foto_url') or auto.foto_url  # Mantiene la URL existente si no se proporciona una nueva
            auto.save()
            formulario.save()  # Guarda el formulario, lo que guarda también el modelo Auto
            return redirect("buscar_auto")  # Redirige a la vista deseada

    return render(request, "editar_auto.html", {"form": formulario, "auto": auto})


# def editar_auto(request, id):
#     auto = Auto.objects.get(id=id) # + request.user.Auto
#     form = config_basica(instance=request.user, initial={"Marca":auto.marca, "Modelo":auto.modelo, "Año":auto.año, "Precio":auto.precio, "Hp":auto.hp, "foto": auto.foto}) #sirve para get
    
#     if request.method == "POST":
#         form = config_basica(request.POST, request.FILES, instance=request.user)  #sirve para post
#         if form.is_valid():
            
#             new_foto = form.cleaned_data.get("foto")
            
#             auto.marca = form.cleaned_data.get("marca")
#             auto.modelo = form.cleaned_data.get("modelo")
#             auto.año = form.cleaned_data.get("año")
#             auto.precio = form.cleaned_data.get("Precio")
#             auto.hp= form.cleaned_data.get("Hp") 
            
#             auto.foto = new_foto if new_foto else auto.foto
            
#         form.save()    
#         auto.save
            
#         return redirect("buscar_auto")
#     return render(request, "editar_auto.html", {"form": form, "auto": auto})
     


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
    form_class = AvionForm
    template_name='editar_avion.html'
    success_url = reverse_lazy("buscar_avion") 


@login_required  
def borrar_avion(request, id):
    avion = Avion.objects.get(id=id)
    avion.delete()
    return redirect("buscar_avion")
