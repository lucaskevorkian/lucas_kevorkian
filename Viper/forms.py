from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Auto, Avion
from django.core.validators import MinValueValidator


class config_basica(forms.Form):
    Marca = forms.CharField(max_length=100, required=False)
    Modelo = forms.CharField(max_length=100, required=False)
    Año = forms.IntegerField(required=False)
    Precio = forms.IntegerField(required=False)
    Hp = forms.IntegerField(required=False)
    
    
class crear_auto_formulario(forms.Form):
    Marca = forms.CharField(max_length=100)
    Modelo = forms.CharField(max_length=100)
    Año = forms.IntegerField(validators=[MinValueValidator(0)], error_messages={'invalid': 'El año no puede ser negativo.'})
    Precio = forms.IntegerField(validators=[MinValueValidator(0)], error_messages={'invalid': 'El año no puede ser negativo.'})
    Hp = forms.IntegerField(validators=[MinValueValidator(0)], error_messages={'invalid': 'El año no puede ser negativo.'})
    
        
class buscar_auto_formulario(config_basica): ...
   

   
class editar_auto_form(forms.ModelForm):
     
    foto = forms.ImageField(required=False)
    
    class Meta:
        model = Auto
        fields = ["marca", "modelo", "año", "precio", "hp", "foto", 'foto_url']
    def clean(self):
        cleaned_data = super().clean()
        foto = cleaned_data.get("foto")
        foto_url = cleaned_data.get("foto_url")

        # Validación: solo uno de los dos puede estar presente
        if foto and foto_url:
            raise forms.ValidationError("Solo se puede subir una imagen: ya sea una foto o una URL, no ambas.") 

        return cleaned_data    
        
class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['modelo', 'año', 'altitud', 'foto']