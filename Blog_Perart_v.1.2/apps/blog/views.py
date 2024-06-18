from django.shortcuts import render

def Index(request):
    return render(request, 'index.html')

def PostList(request):
    return render(request, 'post_list.html')

def PostDetail(request):
    return render(request, 'post_detail.html')

def ProdutoDetail(request):
    return render(request, 'produto_detail.html')

def Navbar(request):
    return render(request, 'navbar.html')