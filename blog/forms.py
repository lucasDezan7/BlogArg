from django import forms
from .models import Blog

class BlogFormulario(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo','sub_titulo','autor','imagen']

class BuscarBlogForm(forms.Form):
    blog = forms.CharField(label='Buscar Post',max_length=120)