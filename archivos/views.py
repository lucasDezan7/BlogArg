from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Archivo
from .forms import ArchivoUploadForm
# Create your views here.

class ArchivoListView(ListView):
    model = Archivo
    template_name = 'archivos/archivo_lista.html'
    context_object_name = 'archivos'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Archivo.objects.filter(titulo__icontains=query)
        return Archivo.objects.all()

class ArchivoDetailView(DetailView):
    model = Archivo
    template_name = 'archivos/archivo_detalle.html'
    context_object_name = 'archivo'

class ArchivoCreateView(CreateView):
    model = Archivo
    form_class = ArchivoUploadForm
    template_name = 'archivos/archivo_form.html'
    success_url = reverse_lazy('archivo_lista')

    def form_valid(self, form):
        form.instance.subido_por = self.request.user
        return super().form_valid(form)

class ArchivoDeleteView(DeleteView):
    model = Archivo
    template_name = 'archivos/archivo_confirmar_borrar.html'
    success_url = reverse_lazy('archivo_lista')