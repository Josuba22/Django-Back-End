from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    imagem_destaque = models.ImageField(upload_to='post/', verbose_name='Imagem em Destaque')
    conteudo = models.TextField(verbose_name='Conteúdo')
    data_publicacao = models.DateTimeField(default=timezone.now, verbose_name='Data de Publicação')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    