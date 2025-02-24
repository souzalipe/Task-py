import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

class ExcelViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Leitor de Excel")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Escolha um arquivo Excel:")
        self.label.pack(pady=5)

        self.btn_open = tk.Button(root, text="Abrir Arquivo", command=self.open_file)
        self.btn_open.pack(pady=5)

        self.label_coluna = tk.Label(root, text="Coluna:")
        self.label_coluna.pack(pady=5)
        self.entry_coluna = tk.Entry(root)
        self.entry_coluna.pack(pady=5)

        self.label_linha = tk.Label(root, text="Linha:")
        self.label_linha.pack(pady=5)
        self.entry_linha = tk.Entry(root)
        self.entry_linha.pack(pady=5)

        self.btn_search = tk.Button(root, text="Buscar Valor", command=self.search_value)
        self.btn_search.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

        self.df = None  # DataFrame inicial

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            try:
                self.df = pd.read_excel(file_path)
                messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível carregar o arquivo.\n{e}")

    def search_value(self):
        if self.df is None:
            messagebox.showwarning("Aviso", "Nenhum arquivo Excel foi carregado!")
            return

        coluna = self.entry_coluna.get()
        linha = self.entry_linha.get()

        try:
            linha = int(linha) - 1  # Ajuste pois o pandas index começa do 0
            valor = self.df.iloc[linha][coluna]
            self.result_label.config(text=f"Valor: {valor}", fg="green")
        except Exception as e:
            self.result_label.config(text="Erro ao buscar!", fg="red")
            messagebox.showerror("Erro", f"Verifique os valores inseridos.\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelViewer(root)
    root.mainloop()