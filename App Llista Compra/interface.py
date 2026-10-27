import streamlit as st
import pandas as pd
import funcao


st.title("Lista de Compras") 

#- criar colunas
colunas = st.columns(2)

#coluna 1
with colunas[0]:
    st.header("Cadastro de Produto")
    nome_produto = st.text_input(label="Digite o nome do Produto:")
    quantidade = st.number_input(label="Digite a quantidade: ",
    min_value=0,
    max_value=100               
    )
    preco_unidade = st.number_input(
        label="Digite o preço unitário: ",
        min_value=0.0,
        max_value=100.00)
# adicionar produto
    if st.button(label="Adicionar produto", use_container_width=True):
        funcao.inserirDados(nome_produto,quantidade,preco_unidade)
        st.success("Produto adicionado")

#coluna 2
with colunas[1]:
    st.header("Apagar Produto ")
    apagar = st.number_input(
        label="Digite o id para apagar",
        min_value=0,
        max_value=100
                            )
#apagar produto
    if  st.button(label="Apagar Produto", use_container_width=True):
        funcao.apagarDado(apagar)
        st.success("Produto apagado com sucesso")
#Listar produtos
if st.button(label="Listar Produtos", use_container_width=True):
    dados = funcao.listarDados()
    tb = pd.DataFrame(dados, columns=("ID", "Quantidade","Produto", "Preço Unidade"))
    
    st.header("Lista de Produtos")
    st.table(tb.style.format({
            "Preço Unidade": "{:.2f}"
        }) )


if st.button(label="Valor Total",use_container_width=True):
    total_compra = 0
    dados = funcao.listarDados()
    for i in dados:
        valorTotal = i[1] * i [3]
        total_compra += valorTotal
    st.write("Valor Total" , total_compra)





st.sidebar.header("Atualizar Preço",)
##st.header()
preco_atualizado = st.sidebar.number_input(
    label="Digite o novo preço",
    format='%1f',
    min_value=0.0,
    max_value=100.00)
    

id_produto = st.sidebar.number_input(
    label="Digite o id do produto para atualizar",
    min_value=0,
    max_value=100)

if st.sidebar.button("Atualizar"):
    funcao.atualizar_preco(preco_atualizado,id_produto)
    st.sidebar.success("Preço Atualizado")


st.sidebar.header("Atualizar Quantidade")
quantidade = st.sidebar.number_input(
    label="Digite a nova quantidade",
    min_value=0,
    max_value=100 )

id_produto_qtde = st.sidebar.number_input(
    label="Digite o id do produto para atualizar", key="id_produto_qtde",
    min_value=0,
    max_value=100)

if st.sidebar.button("Atualizar", key="atualizar_quantidade"):
    funcao.atualizar_qtde(quantidade,id_produto_qtde)
    st.sidebar.success("Quantidade Atualizada")






