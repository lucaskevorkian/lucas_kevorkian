from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class formulario_creacion_usuario(UserCreationForm): #cambios a lo q viene de farica
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir ontraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {key: "" for key in fields}