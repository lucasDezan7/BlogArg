from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def registro(respuesta):
    msj_registro = ''
    if respuesta.method == 'POST':
        form = UserRegisterForm(respuesta.POST)
        if form.is_valid():
            form.save()
            return render(respuesta, 'blog/inicio.html')
        msj_registro = 'Datos incorrectos'
    else:
        form = UserRegisterForm()
    return render(respuesta, 'user/registro.html', {'form': form, 'msj_registro': msj_registro})

def login_respuesta(respuesta):
    msj_login = ''
    if respuesta.method == 'POST':
        form = AuthenticationForm(respuesta, data=respuesta.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(respuesta, user)
                return render(respuesta, 'blog/inicio.html')
            msj_login = 'Contraseña Y/O usuarios incorrectos'
    else:
        form = AuthenticationForm()
    return render(respuesta, 'user/login.html', {'form': form, 'msj_login': msj_login})


@login_required
def Editar(respuesta):
    usuario = respuesta.user

    if respuesta.method == 'POST':
        miform = UserEditForm(respuesta.POST, instance=usuario)
        if miform.is_valid():
            miform.save()
            return render(respuesta, 'blog/inicio.html')
    else:
        miform = UserEditForm(instance=usuario)
    return render(respuesta, 'user/editar.html', {'miform':miform})


class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/editar_contra.html'
    success_url = reverse_lazy('Editar')