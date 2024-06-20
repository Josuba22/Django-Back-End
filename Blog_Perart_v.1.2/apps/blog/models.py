from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('blog:categoria_posts', kwargs={'categoria_slug': self.nome})

class Tag(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('blog:tag_posts', kwargs={'tag_slug': self.nome})

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Rascunho'),
        ('published', 'Publicado'),
    ]

    VISIBILITY_CHOICES = [
        ('public', 'Público'),
        ('private', 'Privado'),
    ]
    
    titulo = models.CharField(max_length=100, verbose_name='Título')
    slug = models.SlugField(unique=True)
    conteudo = models.TextField(verbose_name='Conteúdo')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Autor')
    criado_em = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    visibilidade = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public', verbose_name='Visibilidade')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Categoria', related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
    
    