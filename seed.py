import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema.settings")
django.setup()

from core.models import Cliente, Produto, Venda, ItemVenda

# Criar clientes
for i in range(5):
    Cliente.objects.create(
        nome=f"Cliente {i}",
        email=f"cliente{i}@email.com",
        telefone="47999999999",
        cpf_cnpj=f"0000000000{i}"
    )

# Criar produtos
for i in range(5):
    Produto.objects.create(
        nome=f"Produto {i}",
        descricao="Produto teste",
        preco=random.randint(50, 500),
        estoque=100,
        categoria="Categoria A"
    )

clientes = list(Cliente.objects.all())
produtos = list(Produto.objects.all())

# Criar vendas
for i in range(10):
    venda = Venda.objects.create(
        cliente=random.choice(clientes),
        forma_pagamento="PIX"
    )

    for j in range(random.randint(1,3)):
        produto = random.choice(produtos)
        ItemVenda.objects.create(
            venda=venda,
            produto=produto,
            quantidade=random.randint(1,5),
            preco_unitario=produto.preco
        )

print("Dados criados com sucesso!")