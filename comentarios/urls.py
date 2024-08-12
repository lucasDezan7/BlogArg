from django.urls import path
from .views import agregar_comentario

urlpatterns = [
    path('comentarios/<int:post_id>/agregar', agregar_comentario, name='agregar_comentario'),
]