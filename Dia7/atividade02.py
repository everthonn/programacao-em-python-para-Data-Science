import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import matplotlib.pyplot as plt

conexao = sqlite3.connect('meu_banco_de_dados.db')
cursor = conexao.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        cidade TEXT NOT NULL
    )
''')
conexao.commit()


def inserir_dados():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    cidade = entrada_cidade.get()

    if nome and idade.isdigit() and cidade:
        cursor.execute('INSERT INTO pessoas (nome, idade, cidade) VALUES (?, ?, ?)', (nome, int(idade), cidade))
        conexao.commit()
        messagebox.showinfo("Sucesso", "Dados inseridos com sucesso!")
        entrada_nome.delete(0, tk.END)
        entrada_idade.delete(0, tk.END)
        entrada_cidade.delete(0, tk.END)
        atualizar_tabela()
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos corretamente.")


def exibir_grafico():
    cursor.execute('SELECT nome, idade FROM pessoas')
    dados = cursor.fetchall()
    
    if dados:
        nomes = [dado[0] for dado in dados]
        idades = [dado[1] for dado in dados]

        plt.figure(figsize=(10, 5))
        plt.bar(nomes, idades, color='skyblue')
        plt.xlabel('Nome')
        plt.ylabel('Idade')
        plt.title('Idade das Pessoas')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showwarning("Erro", "Nenhum dado encontrado para exibir.")


def atualizar_tabela():
    for item in tabela.get_children():
        tabela.delete(item)
    
    cursor.execute('SELECT nome, idade, cidade FROM pessoas')
    for row in cursor.fetchall():
        tabela.insert('', tk.END, values=row)

janela = tk.Tk()
janela.title("Cadastro de Pessoas")


tk.Label(janela, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entrada_nome = tk.Entry(janela)
entrada_nome.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Idade:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entrada_idade = tk.Entry(janela)
entrada_idade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Cidade:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entrada_cidade = tk.Entry(janela)
entrada_cidade.grid(row=2, column=1, padx=10, pady=5)


btn_inserir = tk.Button(janela, text="Inserir Dados", command=inserir_dados)
btn_inserir.grid(row=3, column=0, columnspan=2, pady=10)

btn_grafico = tk.Button(janela, text="Exibir Gráfico", command=exibir_grafico)
btn_grafico.grid(row=4, column=0, columnspan=2, pady=10)


tabela = ttk.Treeview(janela, columns=("Nome", "Idade", "Cidade"), show='headings')
tabela.heading("Nome", text="Nome")
tabela.heading("Idade", text="Idade")
tabela.heading("Cidade", text="Cidade")
tabela.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


atualizar_tabela()


janela.mainloop()


conexao.close()
