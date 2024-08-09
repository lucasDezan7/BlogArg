from django.urls import path
from .views import *


urlpatterns = [
    path('', inicio, name='Inicio'),
    path('posteos', BlogListView.as_view(), name='Blog_Posteos'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='Blog_Detalle'),
    path('blog/crear/', BlogCreateView.as_view(), name='Blog_Crear'),
    path('blog/<int:pk>/editar', BlogUpdateView.as_view(), name='blog_Editar'),
    path('blog/<int:pk>/borrar', BlogDeleteView.as_view(), name='blog_Borrar'),
    path('blog/buscar', buscar_Post, name='blog_Buscar'),
]