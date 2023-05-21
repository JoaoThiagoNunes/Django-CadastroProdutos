from django.urls import path
from .views import index, contato_view, produto_view, listProdutos

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato_view, name='contato'),
    path('produto/', produto_view, name='produto'),
    path('listagem/', listProdutos, name='listagem')

]