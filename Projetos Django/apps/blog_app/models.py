from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    conteudo = models.TextField(verbose_name='conteúdo')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    imagem = models.ImageField(upload_to='imagens_posts/', blank=True, null=True, verbose_name='Imagem')

    def __str__(self):
        return self.titulo
    