from django.shortcuts import render, get_object_or_404
from .models import Post, Categoria, Tag

def Index(request):
    return render(request, 'index.html')

def post_list(request):
    posts = Post.objects.filter(status='published', visibilidade='public').order_by('-criado_em')
    context = {'posts': posts}
    return render(request, 'post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published', visibilidade='public')
    context = {'post': post}
    return render(request, 'post_detail.html', context)

def categoria_posts(request, categoria_slug):
    categoria = get_object_or_404(Categoria, name__iexact=categoria_slug)
    posts = categoria.posts.filter(status='published', visibilidade='public').order_by('-criado_em')
    context = {'posts': posts, 'categoria': categoria}
    return render(request, 'categoria_posts.html', context)

def tag_posts(request, tag_slug):
    tag = get_object_or_404(Tag, name__iexact=tag_slug)
    posts = tag.posts.filter(status='published', visibilidade='public').order_by('-criado_em')
    context = {'posts': posts, 'tag': tag}
    return render(request, 'tag_posts.html', context)

def ProdutoDetail(request):
    return render(request, 'produto_detail.html')

def Navbar(request):
    return render(request, 'navbar.html')