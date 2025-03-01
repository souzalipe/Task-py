import sqlite3

def buscar_usuario_por_id(user_id):
    conexao = sqlite3.connect("meubanco.bd")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM clientes WHERE id = ?", (user_id,))
    usuario = cursor.fetchone()

    conexao.close()

    if usuario:
        print("\n--- Cliente encontrado ---")
        print(f"ID: {usuario[0]}")
        print(f"Nome: {usuario[1]}")
        print(f"Idade: {usuario[2]}\n")
    else:
        print("\nCliente não encontrado.\n")

# Loop para permitir múltiplas buscas
while True:
    id_desejado = input("Digite o ID do usuário (ou 'sair' para encerrar): ")

    if id_desejado.lower() == "sair":
        print("Encerrando...")
        break

    if id_desejado.isdigit():
        buscar_usuario_por_id(int(id_desejado))
    else:
        print("Por favor, digite um número válido.\n")
