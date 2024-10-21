from django import forms

class config_basica(forms.Form):
    Marca = forms.CharField(max_length=100, required=False)
    Modelo = forms.CharField(max_length=100, required=False )
    Año = forms.IntegerField(required=False)
    
    
    
class crear_auto_formulario(forms.Form):
    Marca = forms.CharField(max_length=100)
    Modelo = forms.CharField(max_length=100)
    Año = forms.IntegerField()
    
    
        
class buscar_auto_formulario(config_basica): ...
    
    
    
class editar_auto_form(config_basica): ...