from django.db import models

class Celulares(models.Model):
    modelo = models.CharField(max_length=100)
    ano_fabricacao = models.IntegerField(verbose_name='Ano de Fabricação')

    def __str__(self):
        return f"{self.modelo} - {self.ano_fabricacao}"
    