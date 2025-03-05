import sqlite3
import pandas as pd
from tabulate import tabulate  # Para exibição bonita

def buscar_usuario_por_id(user_id):
    conexao = sqlite3.connect("meubanco.db")
    query = f"SELECT * FROM clientes WHERE id = {user_id}"
    df = pd.read_sql_query(query, conexao)
    conexao.close()

    if not df.empty:
        print("\nUsuário encontrado:\n")
        print(tabulate(df, headers="keys", tablefmt="grid"))
    else:
        print("\nUsuário não encontrado.\n")

# Loop para buscar usuários até o usuário decidir sair
while True:
    id_desejado = input("\nDigite o ID do usuário (ou 'sair' para encerrar): ")

    if id_desejado.lower() == "sair":
        print("Saindo do programa... 🚀")
        break  # Sai do loop e encerra o programa

    if id_desejado.isdigit():
        buscar_usuario_por_id(int(id_desejado))
    else:
        print("Por favor, digite um número válido ou 'sair' para encerrar.")
