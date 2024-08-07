# Generated by Django 5.0.6 on 2024-07-02 11:24

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to='fotos/')),
                ('email', models.EmailField(max_length=254)),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='BR')),
                ('mensagem', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
