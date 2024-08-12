from django.shortcuts import render, get_object_or_404, redirect
from .forms import ComentarForm
from comentarios.models import Blog
from django.http import HttpResponseServerError
# Create your views here.

def agregar_comentario(request, post_id):
    try:
        post = get_object_or_404(Blog, id=post_id)
        if request.method == 'POST':
            form = ComentarForm(request.POST)
            if form.is_valid():
                comentario = form.save(commit=False)
                comentario.autor = request.user
                comentario.post = post
                comentario.save()
                return redirect('Blog_Posteos', post_id=post_id)
            else:
                return render(request, 'comentarios/agregar_comentario.html', {'form': form, 'post': post})
        else:
            form = ComentarForm()
            return render(request, 'comentarios/agregar_comentario.html', {'form': form, 'post': post})
    except Exception as e:
        return HttpResponseServerError(f"Ocurrió un error: {e}")