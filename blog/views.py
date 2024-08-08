from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(respuesta):
    return render(respuesta,'blog/inicio.html')

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/blog_lista.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_Detalle.html'


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/BlogCrear.html'
    success_url = reverse_lazy('Blog_Posteos')
    fields = [
        'titulo',
        'sub_titulo',
        'autor',
        'fecha',
        'imagen',
    ]

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog/blog_editar.html'
    success_url = reverse_lazy('Blog_Posteos')
    fields = [
        'titulo',
        'sub_titulo',
        'autor',
        'fecha',
        'imagen',
    ]

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_borrar.html'
    success_url = reverse_lazy('Blog_Posteos')
