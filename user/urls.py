from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('registro/', views.registro, name='Registro'),
    path('login/', views.login_respuesta, name='Login' ),
    path('editar/',views.Editar, name='Editar' ),
    path('cambiarContraseña/',views.CambiarContraseña.as_view(), name='CambiarContraseña' ),
    path('logout/',LogoutView.as_view(template_name='blog/inicio.html'), name='Logout' ),
]