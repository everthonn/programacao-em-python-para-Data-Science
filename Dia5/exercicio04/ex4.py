import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_barra():
    dados = pd.read_csv("Dia5/exercicio04/dados.csv")

    mes = dados["Mês"]
    vendas = dados["Vendas"]
    lucro = dados["Lucro"]

    fig, grafico = plt.subplots()
    grafico.bar(mes, vendas, color='red')
    grafico.set_xlabel('MÊS')
    grafico.set_ylabel('VENDAS')
    grafico.set_title("COMPARAÇÃO VENDAS POR MES")


    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



def plot_pizza():
    dados = pd.read_csv("Dia5/exercicio04/dados.csv")

    mes = dados["Mês"]
    vendas = dados["Vendas"]

    colors = ("red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "white", "gray", "cyan")

    fig, grafico = plt.subplots()
    grafico.pie(vendas, labels=mes, colors=colors, autopct='%1.1f%%')
    grafico.set_title("COMPARAÇÃO ENTRE MESES E VENDAS")


    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)




def plot_linha():
    
    dados = pd.read_csv("Dia5/exercicio04/dados.csv")

    mes = dados["Mês"]
    
    lucro = dados["Lucro"]

    fig, grafico = plt.subplots()
    grafico.plot(mes, lucro, color='red')
    grafico.set_xlabel('MÊS')
    grafico.set_ylabel('LUCRO')
    grafico.set_title("EVOLUÇÃO DOS LUCROS AO LONGO DOS MESES")

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)



def plot_dispersao():
    dados = pd.read_csv("Dia5/exercicio04/dados.csv")

    vendas = dados["Vendas"]
    lucro = dados["Lucro"]

    fig, grafico = plt.subplots()
    grafico.scatter(vendas,lucro, color='red')
    grafico.set_xlabel('VENDAS')
    grafico.set_ylabel('LUCRO')
    grafico.set_title("RELACIONA VENDAS E LUCRO")

    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


    

# Janela criada fora da função
janela = tk.Tk()
janela.title('MOSTRAR GRÁFICO')

# Botão que chama a função
btn = tk.Button(janela, text='GERAR GRÁFICO BARRA', command=plot_barra)
btn.pack(pady=20)

btn2 = tk.Button(janela, text='GERAR GRÁFICO PIZZA', command=plot_pizza)
btn2.pack(pady=20)

btn3 = tk.Button(janela, text='GERAR GRÁFICO LINHA', command=plot_linha)
btn3.pack(pady=20)

btn4 = tk.Button(janela, text='GERAR GRÁFICO DISPERSÃO', command=plot_dispersao)
btn4.pack(pady=20)

janela.mainloop()
