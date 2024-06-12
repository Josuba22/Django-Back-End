from django.shortcuts import render, get_object_or_404
from .models import Post

def listar_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/listar_posts.html', {'posts': posts})

def detalhe_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog_app/detalhe_post.html', {'post': post})