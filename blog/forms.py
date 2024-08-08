from django import forms
from .models import Blog

class BlogFormulario(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo','sub_titulo','autor','imagen']