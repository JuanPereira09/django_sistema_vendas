from django.contrib import admin
from .models import Cliente, Produto, Venda, ItemVenda

class ItemVendaInline(admin.TabularInline):
    model = ItemVenda
    extra = 1


@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    inlines = [ItemVendaInline]
    list_display = ('id', 'cliente', 'data', 'forma_pagamento', 'valor_total')
    readonly_fields = ('valor_total',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cpf_cnpj', 'data_cadastro')
    search_fields = ('nome', 'cpf_cnpj')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'estoque')
    search_fields = ('nome',)
    list_filter = ('categoria',)


@admin.register(ItemVenda)
class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ('venda', 'produto', 'quantidade', 'preco_unitario')