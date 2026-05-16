from django.db import models

from django.contrib.auth.models import User

class Artigo(models.Model):
    texto = models.TextField()
    imagem = models.ImageField(upload_to="artigos", blank=True)
    link_externo = models.URLField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    likes = models.ManyToManyField(User, related_name="artigos_likes", blank=True)

    def __str__(self):
        return self.texto

    def total_likes(self):
        return self.likes.count();

class Comentario(models.Model):
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name="comentarios")

    def __str__(self):
        return self.texto