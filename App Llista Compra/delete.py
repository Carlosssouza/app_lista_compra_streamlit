import sqlite3
conexao = sqlite3.connect("banco_compra.db")
cursor = conexao.cursor()

conexao.execute("DROP TABLE IF EXISTS produto")
conexao.commit()
conexao.close()
print("Tabela excluida com sucesso")