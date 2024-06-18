from django.urls import path
from .views import *

urlpatterns = [
    path("", ViewsIndex),
    path("post_list", ViewsPostList)
]
