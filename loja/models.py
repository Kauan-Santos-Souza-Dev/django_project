from django.db import models

# Create your models here.

# Cada classe vira uma tabela 
# cada atributo da classe vira uma coluna.

# Instalar o Driver: o “tradutor” entre o Python/Django e o MySQL.
## pip install mysqlclient

# Modelos são classes que representam tabelas no banco de dados. Cada atributo da classe representa uma coluna na tabela.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome