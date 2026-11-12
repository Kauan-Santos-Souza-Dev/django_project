# Importa o módulo admin do Django e o modelo Produto do arquivo models.py.
from django.contrib import admin
from .models import Produto

# O admin.py só diz quais models aparecem no painel.
# Superusuário: a conta que tem permissão para entrar no painel (fica em /admin/).

# Cria a folha de instruções.
class ProdutoAdmin(admin.ModelAdmin):
    # É uma tupla com os campos de texto onde o Admin vai procurar. Ao definir, aparece uma caixa de busca acima da lista.
    list_display = ('nome', 'preco', 'descricao', 'estoque', 'ativo')

    search_fields = ('nome', 'descricao')  # Define quais campos serão pesquisáveis na lista de produtos.
    list_filter = ('ativo',)  # Define quais campos serão filtráveis na lista de produtos.
    ordering = ('nome',)  # Define a ordem de exibição dos produtos na lista.
    list_editable = ('preco', 'estoque', 'ativo')  # Define quais campos serão editáveis diretamente na lista de produtos.
    fieldsets = [
        ('Informações básicas', {'fields': ('nome', 'descricao')}),
        ('Venda e estoque', {'fields': ('preco', 'estoque', 'ativo')}),
    ]
admin.site.site_header = 'Painel de Administração da loja'  # ele define o texto grande no topo do painel.
admin.site.site_title = 'Administrador'  # ele define o texto que aparece na aba do navegador.
admin.site.index_title = 'Gerenciamento da loja'

# Entrega a folha ao Admin
admin.site.register(Produto, ProdutoAdmin)  # Registra o modelo Produto com a classe ProdutoAdmin e o site personalizado MeuAdminSite.



