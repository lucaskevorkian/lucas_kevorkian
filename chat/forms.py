 
from django import forms
from .models import Mensaje

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['contenido', 'receptor']  # Suponiendo que quieras que el usuario seleccione un receptor
