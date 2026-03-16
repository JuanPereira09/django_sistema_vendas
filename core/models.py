from django.db import models
from django.db.models import Sum, F

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20)
    cpf_cnpj = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    FORMA_PAGAMENTO = (
        ('DINHEIRO', 'Dinheiro'),
        ('CARTAO', 'Cartão'),
        ('PIX', 'Pix'),
    )

    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    forma_pagamento = models.CharField(max_length=20, choices=FORMA_PAGAMENTO)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def atualizar_total(self):
        total = self.itens.aggregate(
            total=Sum(F('quantidade') * F('preco_unitario'))
        )['total']

        self.valor_total = total or 0
        super().save()

    def __str__(self):
        return f"Venda {self.id}"
    
class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):

        # definir preço se não existir
        if not self.preco_unitario:
            self.preco_unitario = self.produto.preco

        super().save(*args, **kwargs)

        # baixar estoque
        produto = self.produto
        produto.estoque -= self.quantidade
        produto.save()

        # atualizar total da venda
        if hasattr(self.venda, 'atualizar_total'):
            self.venda.atualizar_total()

    def subtotal(self):
        return self.quantidade * self.preco_unitario
