 
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('chat:ver_mensajes')  # Cambié aquí para incluir el espacio de nombres
    else:
        form = MensajeForm()
    
    return render(request, 'chat/enviar_mensaje.html', {'form': form})

@login_required
def ver_mensajes(request): 
    mensajes_recibidos = Mensaje.objects.filter(receptor=request.user).order_by('-fecha_creacion')
    return render(request, 'chat/ver_mensajes.html', {'mensajes': mensajes_recibidos})
 

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

 