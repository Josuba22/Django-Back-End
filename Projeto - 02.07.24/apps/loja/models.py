from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Produto')
    foto_produto = models.ImageField(upload_to='produtos/', blank=True, verbose_name='Foto do Produto')
    descricao = models.TextField(verbose_name='Descrição')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço')

    def __str__(self):
        return self.nome
    