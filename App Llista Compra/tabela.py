import sqlite3
conexao = sqlite3.connect("banco_compra.db")
cursor = conexao.cursor()

comando_sql = """ 
CREATE TABLE IF NOT EXISTS produto(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    quantidade NUM NOT NULL,
    nome_produto TEXT NOT NULL,
    preco_unidade REAL NOT NULL
);
"""
cursor.execute(comando_sql)
cursor.close()
print("Tabela criada com sucesso")