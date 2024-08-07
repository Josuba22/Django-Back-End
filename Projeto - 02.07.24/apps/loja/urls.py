from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('produto/<int:produto_id>/', detalhes_produto, name='detalhes_produto'),
    path('adicionar_produto/', adicionar_produto, name='adicionar_produto'),
    path('adicionar_categoria/', adicionar_categoria, name='adicionar_categoria'),
    path('excluir-produto/<int:id_produto>', ExcluirProduto, name='conf_excluir_produto'),
    path('editar-produto/<int:id_produto>', EditarProduto, name='pg_editar_produto'),
]
