from django.shortcuts import render, redirect
from .models import Auto
from .forms import crear_auto_formulario, buscar_auto_formulario, config_basica
def index(request):
    return render(request, 'index.html')


def sobre_mi(request):
    return render(request, "sobre_mi.html")

def precio(request):
    return render(request, "precio.html")


def buscar_auto(request):
    formulario = buscar_auto_formulario(request.GET)
    
    if formulario.is_valid():
        marca = formulario.cleaned_data.get("Marca")
        modelo = formulario.cleaned_data.get("Modelo")
        año = formulario.cleaned_data.get("Año")

        # Construimos el diccionario de filtros
        filtros = {}
        if marca:
            filtros['marca__icontains'] = marca  # Buscamos coincidencias parciales de marca
        if modelo:
            filtros['modelo__icontains'] = modelo  # Buscamos coincidencias parciales de modelo
        if año is not None:  # Comprobamos que año no sea None
            filtros['año'] = año

        # Aplicamos los filtros a la consulta
        autos = Auto.objects.filter(**filtros)  # Descomponemos el diccionario en clave=valor
        
    # else: REEMPLAZADO POR EL __ICONTAINS
    #     autos = Auto.objects.all()
    
    return render(request, "buscar_auto.html", {"autos": autos, "form": formulario})



def crear_auto(request):
    
    # print("Request", request)  APARECE EN LA TERMINAL
    # print("GET", request.GET)
    # print("POST", request.POST)
    
    formulario = crear_auto_formulario()

    
    if request.method == "POST":
        
        formulario = crear_auto_formulario(request.POST)
        if formulario.is_valid():  
            data = formulario.cleaned_data
            auto = Auto(marca=data.get("Marca"), modelo=data.get("Modelo"), año=data.get("Año"))
            auto.save()
            return redirect("buscar_auto")
            
            
            
        return render(request, "crear_auto.html", {"form": formulario})
    return render(request, "crear_auto.html", {"form": formulario})
    
    
def ver_auto(request, id):
    auto = Auto.objects.get(id=id)
    return render(request, "ver_auto.html", {"auto": auto})
    
    
def borrar_auto(request, id):
    auto = Auto.objects.get(id=id)
    auto.delete()
    return redirect("buscar_auto")

  
def editar_auto(request, id):
    auto = Auto.objects.get(id=id)
    
    form = config_basica(initial={"Marca":auto.marca, "Modelo":auto.modelo, "Año":auto.año}) #sirve para get
    
    if request.method == "POST":
        form = config_basica(request.POST)  #sirve para post
        if form.is_valid():
            auto.marca = form.cleaned_data.get("marca")
            auto.modelo = form.cleaned_data.get("modelo")
            auto.año = form.cleaned_data.get("año")
             
        auto.save
            
        return redirect("buscar_auto")
    return render(request, "editar_auto.html", {"form": form, "auto": auto})
    
    
    # FUNCIONA TAMBIEN
    # Usar request.POST.get para evitar MultiValueDictKeyError
    # marca = request.POST.get("Marca")
    # modelo = request.POST.get("Modelo")
    # año = request.POST.get("Año")
    
    # Validar que los campos no estén vacíos
    # if marca and modelo and año:
        # auto = Auto(marca=marca, modelo=modelo, año=año)
        # auto.save()
        # return render(request, "crear_auto.html", {"mensaje": "Auto creado exitosamente"})
    # else:
    #     return render(request, "crear_auto.html", {"error": "Faltan datos en el formulario"})



        
        