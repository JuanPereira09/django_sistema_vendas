from django.urls import path
from .views import dashboard, nova_venda, adicionar_itens, finalizar_venda, lista_produtos, novo_produto, relatorio_vendas, pagina_relatorio
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', dashboard, name='dashboard'),

    path('nova-venda/', nova_venda, name='nova_venda'),
    path('venda/<int:venda_id>/itens/', adicionar_itens, name='adicionar_itens'),
    path('venda/<int:venda_id>/finalizar/', finalizar_venda, name='finalizar_venda'),

    path('produtos/', lista_produtos, name='produtos'),
    path('produto/novo/', novo_produto, name='novo_produto'),
    path('relatorio/vendas/', relatorio_vendas, name='relatorio_vendas'),
    path('relatorios/', pagina_relatorio, name='pagina_relatorio'),

]