from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class formulario_creacion_usuario(UserCreationForm): #cambios a lo q viene de farica
    email = forms.EmailField()
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir ontraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]
        help_texts = {key: "" for key in fields}
        
        
        
class formulario_edicion_perfil(UserChangeForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    password = None
    avatar = forms.ImageField(required=False)
    
    class Meta():
        model = User
        fields = ["email", "first_name", "last_name", "avatar"] 