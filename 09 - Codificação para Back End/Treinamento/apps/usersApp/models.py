from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('active', 'Ativo'),
    ('inactive', 'Inativo'),
    ('banned', 'Banido'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.user.username
    