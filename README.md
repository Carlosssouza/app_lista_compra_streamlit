# Aplicativo de Lista de Compra
Aplicação desenvolvida em Python, Streamlit para interface e SQLite para armazenamento dos dados, para gerenciar uma lista de compras, permitindo ao usuário cadatsrar,consultar, atualizar e excluir produtos, preços e quantidade, além de visualizar as informações em uma interface simples e intuitiva.

O projeto foi desenvolvido com objetivo de praticar conceitos de programação, manipulação de banco de dados.

## Funcionalidades

- Cadastrar produtos.

- Listar os produtos cadastrados.

- Atualizar informações dos produtos.

- Excluir produtos pelo ID.

- Armazenar os dados em um banco de dados SQLite.

- Exibir os produtos em uma tabela na interface.

- Calcular o valor total das compras, caso essa funcionalidade esteja implementada.

###  Tecnologias utilizadas

- Python: linguagem de programação utilizada no desenvolvimento.

- Streamlit: criação da interface web interativa.

- SQLite: armazenamento e gerenciamento dos dados.

- Pandas: organização e exibição dos dados em tabelas, quando utilizado.

#### Estrutura do projeto

App Llista Compra/

├── interface.py

├── funcao.py

├── main.py

├── delete.py

├── tabela.py

├── requirements.txt

└── banco_compra.db

##### Descrição dos arquivos

- interface.py: interface do aplicativo desenvolvida com Streamlit.

- funcao.py: funções responsáveis pelas operações com o banco de dados.

- main.py: criação do banco de dados em SQLite

- delete.py: operações relacionadas à exclusão de produtos.

- tabela.py: criação da tabela produtos no banco de dados.

- requirements.txt: lista de bibliotecas necessárias para executar o projeto.

- banco_compra.db: banco de dados SQLite utilizado para armazenar os produtos.

###### Como executar o projeto

1. Pré-requisitos

      Python instalado.

      Git instalado, caso queira clonar o repositório.

2. Clone o repositório

      git clone URL_DO_SEU_REPOSITORIO

3. Entre na pasta do projeto

      cd "App Llista Compra"

4. Instale as dependências

      pip install -r requirements.txt

5. Execute o aplicativo

      streamlit run interface.py
   
Após a inicialização, o Streamlit exibirá o endereço local para acessar o aplicativo pelo navegador.

####### Aprendizados

- Durante o desenvolvimento deste projeto, pratiquei:

- Lógica de programação com Python.

- Criação e utilização de funções.

- Operações CRUD (Create, Read, Update e Delete).

- Integração entre Python e SQLite.

- Criação de interfaces com Streamlit.

- Organização de dados com Pandas.

######## Autor

- Desenvolvido por Carlos Silva Souza.

