from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class formulario_creacion_usuario(UserCreationForm): #cambios a lo q viene de farica
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {key: "" for key in fields}
        
        
        
class formulario_edicion_perfil(UserChangeForm):
    email = forms.EmailField(label="Email", required=False)
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    fecha_nacimiento = forms.DateField(required=False)
    password = None
    avatar = forms.ImageField(required=False)
    
    class Meta():
        model = User
        fields = ["email", "first_name", "last_name", "fecha_nacimiento", "avatar"] 