from django import forms
from .models import Produto

# forms.Form é a classe base. Herdando dela, a sua classe ganha toda a lógica de validação.
class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    email = forms.EmailField(label='Email')
    mensagem = forms.CharField(widget=forms.Textarea, label='Mensagem')

# Constrói um Form apartir de um model.
class ProdutoForm(forms.ModelForm):
    # Configurar o formulário para o modelo Produto.
    class Meta:
        # De qual model construir o form.
        model = Produto
        # Quais campos do model vão aparecer no form.
        fields = ['nome', 'descricao', 'preco', 'estoque', 'ativo']