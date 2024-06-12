from django.db import models

TIPO_SEXO = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

class Estudante(models.Model):
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=2, choices=TIPO_SEXO, blank=True, null=True)
    valor = models.DecimalField(decimal_places=2, max_digits=4, default=0.00)
    foto = models.ImageField(upload_to='foto_perfil/', blank=True, null=True)

    def __str__(self):
        return self.nome
    