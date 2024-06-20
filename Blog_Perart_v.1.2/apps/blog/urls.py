from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', post_detail, name='post_detail')
]
