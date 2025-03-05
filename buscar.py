import sqlite3
import pandas as pd
from tabulate import tabulate  # Biblioteca para exibição bonita

def buscar_usuario_por_id(user_id):
    conexao = sqlite3.connect("meubanco.bd")
    query = f"SELECT * FROM clientes WHERE id = {user_id}"
    df = pd.read_sql_query(query, conexao)
    conexao.close()

    if not df.empty:
        print("\nUsuário encontrado:\n")
        print(tabulate(df, headers="keys", tablefmt="grid"))  # Formato de tabela
    else:
        print("\nUsuário não encontrado.\n")

id_desejado = input("Digite o ID do usuário: ")
if id_desejado.isdigit():
    buscar_usuario_por_id(int(id_desejado))
else:
    print("Por favor, digite um número válido.")
