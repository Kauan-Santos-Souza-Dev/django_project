# O ponto signfica que o arquivo urls.py está no mesmo diretório que o arquivo views.py
# Esse arquivo urls.py é responsável por mapear as URLs para as views correspondentes

from django.urls import path
from . import views

# urlpatterns é uma lista de objetos path() que mapeiam URLs para views. Cada objeto path() recebe três argumentos: a URL, a view correspondente e um nome opcional para a URL.
urlpatterns = [
    # <int:id>/ aqui pode vir um número inteiro, e eu vou chamar esse número de id”.
        path('produtos/', views.lista_produtos, name='lista_produtos'),
        path('produtos/<int:id>/', views.detalhe_produto, name='detalhe_produto'),
        path('teste_reverse/', views.teste_reverse, name='teste_reverse'),
        path('', views.home, name='home'), 
        path('contato/', views.contato, name='contato'),
        path('produtos/novo/', views.novo_produto, name='novo_produto'),
        path('api/produtos/', views.api_produtos, name='api_produtos'),
        # O <int:id> captura o número da URL e o entrega à view no parâmetro id. Se alguém acessar /api/produtos/3/, a view recebe id=3.
        path('api/produtos/<int:id>/', views.api_produtos_detalhes, name='api_produto_detalhe'),
]
