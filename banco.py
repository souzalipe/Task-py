import sqlite3

# Criando o banco de dados/ Conectando ao banco de dados

conexao = sqlite3.connect('meubanco.bd')
cursor = conexao.cursor()

# Criando uma tabela 

cursor.execute("""
               CREATE TABLE IF NOT EXISTS clientes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER
               )
               """)

# Inserindo dados na tabela

cursor.execute("INSERT INTO clientes (nome, idade) VALUES ('Felipe', 25)")
cursor.execute("INSERT INTO clientes (nome, idade) VALUES ('Débora', 22)")
cursor.execute("INSERT INTO clientes (nome, idade) VALUES ('Brenda', 28)")

# Salvando as alterações

conexao.commit()
conexao.close()

print('Banco de dados criado com sucesso!')