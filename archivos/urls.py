from django.urls import path
from .views import ArchivoListView, ArchivoDetailView, ArchivoCreateView, ArchivoDeleteView

urlpatterns = [
    path('archivos/', ArchivoListView.as_view(), name='archivo_lista'),
    path('<int:pk>/', ArchivoDetailView.as_view(), name='Archivo_detalle'),
    path('cargas/', ArchivoCreateView.as_view(), name='Archivo_crear'),
    path('<int:pk>/borrar/', ArchivoDeleteView.as_view(), name='Archivo_borrar'),
]