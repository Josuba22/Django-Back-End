from django.db import models
from django.contrib.auth.models import User  # Importe o modelo User
from django.utils import timezone

class CategoriaBlog(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(max_length=255, unique=True)  # Para URLs amigáveis
    conteudo = models.TextField(verbose_name='Conteúdo')
    imagem_destaque = models.ImageField(upload_to='posts/', blank=True, verbose_name='Imagem em Destaque')
    data_publicacao = models.DateTimeField(default=timezone.now, verbose_name='Data de Publicação')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Autor')  # Relacionamento com User
    categorias = models.ManyToManyField(CategoriaBlog, verbose_name='Categoria')

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios', verbose_name='Post')
    autor = models.CharField(max_length=100, verbose_name='Autor')
    email = models.EmailField(verbose_name='E-mail')
    corpo = models.TextField(verbose_name='Corpo')
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'Comentário de {self.autor} em {self.post}'