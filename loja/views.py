from django.shortcuts import render , redirect, get_object_or_404 
from django.urls import reverse
from django.http import HttpResponse, Http404
# O . significa “da mesma pasta (app) onde este arquivo está”. É o jeito de a view enxergar o Produto.
from .models import Produto
from .forms import ContatoForm, ProdutoForm

# Create your views here.
# Exectua a lógica de negócios e retorna uma resposta HTTP

from django.http import HttpResponse

# View 1: 
def lista_produtos(request):
    # O método GET é usado para buscar informações do servidor. Ele é o método padrão quando você acessa uma página web.
    # Ele devolve o valor de q, ou '' se o parâmetro não vier na URL.
    busca = request.GET.get('q', '')
    # O método GET é usado para buscar informações do servidor. Ele é o método padrão quando você acessa uma página web.
    produtos = Produto.objects.filter(nome__icontains=busca) # o que o usuário digitou aparece dentro do nome deste produto?
    return render(request, 'loja/lista.html', {'busca': busca , 'produtos': produtos})

# View 2:
# O método reverse transforma o apelido no endereço.
def teste_reverse(request):
    # Reverse é uma função do Django que recebe o nome da URL e retorna o endereço correspondente.
    endereco = reverse('detalhe_produto', args=[5]) # Args é uma lista de argumentos que serão passados para a URL. 
    return HttpResponse(f"O endereço de detalhe_produto é: {endereco}")

# View 3: Se o produto não existir, levanta uma exceção Http404. Caso contrário, retorna o nome e o preço do produto.
def detalhe_produto(request, id):
        produto = get_object_or_404(Produto, id=id) # faz Produto.objects.get(id=id) e, se levantar DoesNotExist, já lança o 404 sozinho.
        return render(request, 'loja/detalhe.html', {'produto': produto})

# View 4: # Redireciona para a rota lista_produtos
def home(request): 
    return redirect('lista_produtos')  

# View 5: A views 5 permite que o usuário envie uma mensagem de contato.
def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            return HttpResponse(f"Obrigado, {nome}! Mensagem recebida.")
    else:
        form = ContatoForm()
    return render(request, 'loja/contato.html', {'form': form})

# View 6: A views 6 permite que o usuário adicione um novo produto.
def novo_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save()
            # DEPOIS DE SALVAR O PRODUTO, REDIRECIONA PARA A PÁGINA DE DETALHE DO PRODUTO.
            return redirect('detalhe_produto', produto.id)
    else:
        form = ProdutoForm()
    return render(request, 'loja/novo_produto.html', {'form': form})