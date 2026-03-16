# Sistema de Controle de Clientes e Vendas (Django)

Projeto desenvolvido em **Python + Django** para gerenciamento simples de:

* Clientes
* Produtos
* Vendas
* Relatórios

O objetivo é criar um **sistema administrativo completo**, semelhante a pequenos ERPs utilizados por empresas.

---

# Funcionalidades

### Usuários

* Login
* Logout
* Controle de acesso

### Clientes

* Cadastro de clientes
* Nome
* Email
* Telefone
* CPF/CNPJ
* Data de cadastro

### Produtos

* Cadastro de produtos
* Nome
* Descrição
* Preço
* Estoque
* Categoria

### Vendas

* Registro de vendas
* Seleção de cliente
* Adição de produtos
* Cálculo automático do valor total
* Atualização automática de estoque

### Relatórios

* Exportação de vendas para **Excel**
* Filtro por **período**
* Total de faturamento

### Dashboard

* Visão geral do sistema
* Total de clientes
* Total de produtos
* Total de vendas

---

# Tecnologias utilizadas

* Python 3
* Django
* SQLite
* OpenPyXL (geração de Excel)

---

# Instalação

Clone o repositório:

```
git clone https://github.com/SEU_USUARIO/django_sistema_vendas.git
```

Entre na pasta:

```
cd django_sistema_vendas
```

Crie ambiente virtual:

```
python -m venv venv
```

Ative o ambiente:

Windows:

```
venv\Scripts\activate
```

Instale dependências:

```
pip install django openpyxl
```

Rode as migrações:

```
python manage.py migrate
```

Crie um usuário administrador:

```
python manage.py createsuperuser
```

Inicie o servidor:

```
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000
```

Admin:

```
http://127.0.0.1:8000/admin
```

---

# Estrutura do Projeto

```
core/       -> Models, views e lógica do sistema
sistema/    -> Configuração do Django
templates/  -> Templates HTML
```

---

# Melhorias futuras

* Dashboard com gráficos
* Relatórios avançados
* Controle de estoque mais detalhado
* Interface moderna com Bootstrap
* Sistema de permissões por usuário
* API REST

---

# Licença

Projeto de estudo e desenvolvimento pessoal.
