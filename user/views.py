from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def registro(request):
    msj_registro = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/inicio.html')
        msj_registro = 'Datos incorrectos'
    else:
        form = UserRegisterForm()
    return render(request, 'user/registro.html', {'form': form, 'msj_registro': msj_registro})

def login_request(request):
    msj_login = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                return render(request, 'blog/inicio.html')
            msj_login = 'Contraseña Y/O usuarios incorrectos'
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'msj_login': msj_login})


@login_required
def Editar(request):
    usuario = request.user

    if request.method == 'POST':
        miform = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miform.is_valid():
            if miform.cleaned_data.get('imagen'):
                usuario.avatar.imagen = miform.cleaned_data.get('imagen')
                usuario.avatar.save()
            miform.save()
            return render(request, 'blog/inicio.html')
    else:
        miform = UserEditForm(instance=usuario)
    return render(request, 'user/editar.html', {'miform':miform})


class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/editar_contra.html'
    success_url = reverse_lazy('Editar')