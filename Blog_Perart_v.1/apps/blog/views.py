from django.shortcuts import render, get_object_or_404
from .models import Post, CategoriaBlog

def post_list(request):
    posts = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('-data_publicacao')
    categorias = CategoriaBlog.objects.all()
    context = {'posts': posts, 'categorias': categorias}
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)

def categoria_detail(request, categoria_id):
    categoria = get_object_or_404(CategoriaBlog, pk=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    context = {'categoria': categoria, 'posts': posts}
    return render(request, 'blog/categoria_detail.html', context)