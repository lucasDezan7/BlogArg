from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BuscarBlogForm


def inicio(request):
    return render(request,'blog/inicio.html')

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/blog_lista.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


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

def buscar_Post(request):
    form = BuscarBlogForm()
    resultado = None

    if request.method == 'GET':
        form = BuscarBlogForm(request.GET)
        if form.is_valid():
            busqueda = form.cleaned_data['blog']
            resultado = Blog.objects.filter(titulo__icontains = busqueda)
    return render(request, 'blog/blog_buscar.html', {'form':form, 'resultados': resultado})