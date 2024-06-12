from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

STATUS_CHOICES = (
    ('draft', 'Rascunho'),
    ('published', 'Publicado'),
)

VISIBILITY_CHOICE = (
    ('public', 'Público'),
    ('private', 'Privado'),
)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    criado_em = models.DateTimeField(default=timezone.now)
    update_em = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    visibilidade = models.CharField(max_length=10, choices=VISIBILITY_CHOICE, default='public')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)

    def __str__(self):
        return self.titulo
    