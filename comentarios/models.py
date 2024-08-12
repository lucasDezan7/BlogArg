from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog
# Create your models here.
class Comentar(models.Model):
    post = models.ForeignKey(Blog, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor} comento en el post de {self.post}'