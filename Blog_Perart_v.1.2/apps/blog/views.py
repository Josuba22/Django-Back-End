from django.shortcuts import render

def ViewsIndex(request):
    return render(request, 'index.html')

def ViewsPostList(request):
    return render(request, 'post_list.html')

def ViewsPostDetail(request):
    return render(request, 'post_detail.html')

def ViewProdutoDetail(request):
    return render(request, 'produto_detail.html')

def ViewNavbar(request):
    return render(request, 'navbar.html')