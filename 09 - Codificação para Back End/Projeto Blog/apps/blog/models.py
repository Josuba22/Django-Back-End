from django.db import models

STATUS_CHOICES = (
    ('rascunho', 'Rascunho'),
    ('publicado', 'Publicado')
)

class Post(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Título')
    slug = models.SlugField(max_length=100, unique=True)
    autor = models.CharField(max_length=100)
    conteudo = models.TextField(verbose_name='Conteúdo')
    data_publi = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='rascunho')

    def __str__(self):
        return self.titulo
    