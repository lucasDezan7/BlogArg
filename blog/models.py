from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    titulo = models.CharField(max_length=120)
    sub_titulo = models.CharField(max_length=70)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='blog_imagenes')

    def __str__(self):
        return self.titulo