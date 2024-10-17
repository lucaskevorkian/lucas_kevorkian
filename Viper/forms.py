from django import forms


class MiFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    
class crear_auto_formulario(forms.Form):
    Marca = forms.CharField(max_length=100)
    Modelo = forms.CharField(max_length=100)
    Año = forms.IntegerField()
    
    
        
class buscar_auto_formulario(forms.Form):
    Marca = forms.CharField(max_length=100, required=False)
    Modelo = forms.CharField(max_length=100, required=False )
    Año = forms.IntegerField(required=False)