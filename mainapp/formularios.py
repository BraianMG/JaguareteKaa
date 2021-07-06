from django import forms
from django.core import validators

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormRegistro(UserCreationForm):
    username = forms.CharField(label='Usuario',
                               widget=forms.TextInput(attrs={'type':'text', 'class':'form-control', 'id':'usuario'}),
                               max_length=150,
                               required=True,
                               help_text='Requerido. 150 caracteres o menos. Letras, dígitos y @ /. / + / - / _ solamente.')
    email = forms.EmailField(label='Email',
                             widget=forms.TextInput(attrs={'type':'email', 'class':'form-control', 'id':'email'}),
                             max_length=254,
                             required=True,
                             help_text='Se requiere una direccion de email valida.')
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'type':'password', 'class':'form-control', 'id':'contrasenia1'}),
                                max_length=128,
                                required=True,
                                help_text='Requerido. Al menos 8 caracteres y no pueden ser todos numeros.')
    password2 = forms.CharField(label='Repetir Password',
                                widget=forms.PasswordInput(attrs={'type':'password', 'class':'form-control', 'id':'contrasenia2'}),
                                max_length=128,
                                required=True,
                                help_text='Requerido. Ingrese la misma contraseña que antes, para verificación.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')