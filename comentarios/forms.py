from django import forms
from .models import Comentar

class ComentarForm(forms.ModelForm):
    class Meta:
        model = Comentar
        fields = ['texto']