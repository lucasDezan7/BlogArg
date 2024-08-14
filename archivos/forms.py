from django import forms
from .models import Archivo

class ArchivoUploadForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ['titulo','archivo']