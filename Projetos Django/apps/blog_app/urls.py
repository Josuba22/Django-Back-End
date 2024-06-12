from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_posts, name='listar_posts'),
    path('<int:post_id>/', views.detalhe_post, name='detalhe_post'),
]
