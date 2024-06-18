from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('posts/', PostList, name='post_list'),
    path('posts/<int:pk>/', PostDetail, name='post_detail')
]
