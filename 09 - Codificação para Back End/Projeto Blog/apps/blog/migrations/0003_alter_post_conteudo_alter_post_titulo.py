# Generated by Django 5.0.6 on 2024-06-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=models.TextField(verbose_name='Conteúdo'),
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]
