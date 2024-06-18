from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='blog_post_list'),
    path('<slug:slug>/', views.post_detail, name='blog_post_detail'),
    path('categoria/<int:categoria_id>/', views.categoria_detail, name='blog_categoria_detail'),
]