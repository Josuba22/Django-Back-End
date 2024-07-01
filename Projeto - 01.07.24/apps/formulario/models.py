from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Lead(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/')
    email = models.EmailField()
    telefone = PhoneNumberField(region='BR')
    mensagem = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome