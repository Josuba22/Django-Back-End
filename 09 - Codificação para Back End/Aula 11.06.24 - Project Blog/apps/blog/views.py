from django.shortcuts import render
from .models import Post

def lista_posts(request):
    posts = Post.objects.all().order_by('-data_publicacao')
    return render(request, 'lista_posts.html', {'posts': posts})