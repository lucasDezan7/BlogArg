from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Archivo(models.Model):
    titulo = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='cargas')
    subido_en = models.DateField(auto_now_add=True)
    subido_por = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.titulo