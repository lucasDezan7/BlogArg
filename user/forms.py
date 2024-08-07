from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label='Email')
    last_name = forms.CharField(label='Apellido', required=False)
    first_name = forms.CharField(label='Nombre', required=False)
    imagen = forms.ImageField(label='Imagen', required=False)

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'imagen']

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
