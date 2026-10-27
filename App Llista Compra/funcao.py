import sqlite3

def conectaBD():
    conexao = sqlite3.connect("banco_compra.db")
    return conexao

def inserirDados(produto, quantidade, preco_unid):
    conexao = conectaBD()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produto(nome_produto, quantidade, preco_unidade) VALUES (?,?,?)", (produto,quantidade,preco_unid))
    conexao.commit()
    conexao.close()

def listarDados():
    conexao = conectaBD()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM produto")
    dados = cursor.fetchall()
    cursor.close()
    return dados

def apagarDado(id):
    conexao = conectaBD()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM produto WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

def atualizar_preco(preco_unidade,id):
    conexao = conectaBD()
    cursor = conexao.cursor()
    cursor.execute("UPDATE produto SET  preco_unidade = ? WHERE id = ?",(preco_unidade, id))
    conexao.commit()
    conexao.close()
    
def atualizar_qtde(quantidade,id):
    conexao = conectaBD()
    cursor = conexao.cursor()
    cursor.execute("UPDATE produto SET  quantidade = ? WHERE id = ?",(quantidade, id))
    conexao.commit()
    conexao.close()