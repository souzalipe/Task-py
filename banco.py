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
cursor.execute("INSERT INTO clientes (nome, idade) VALUES ('Jonas', 56)")

# Inserindo vários dados de uma vez

cursor.execute("""
    INSERT INTO clientes (nome, idade) VALUES 
    ('Lucas', 34), ('Mariana', 25), ('João', 40), ('Ana', 22), ('Carlos', 29), 
    ('Fernanda', 37), ('Ricardo', 31), ('Camila', 27), ('Felipe', 30), ('Larissa', 26), 
    ('Gustavo', 33), ('Tatiane', 24), ('Eduardo', 28), ('Beatriz', 35), ('Rafael', 32), 
    ('Juliana', 23), ('Pedro', 41), ('Vanessa', 29), ('Bruno', 36), ('Carolina', 21)
""")

# Salvando as alterações

conexao.commit()
conexao.close()

print('Banco de dados criado com sucesso!')