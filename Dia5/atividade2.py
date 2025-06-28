# import pandas as pd
# import matplotlib as plt
# import tkinter as tk
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# def plot_data():
#     dados = pd.read_csv('dados.csv')

#     ano = dados["Ano"]
#     vendas = dados["Vendas"]

#     fig,grafico = plt.suplots()


#     grafico.plot(ano,vendas, marker = 'o',color = 'red')
#     grafico.bar(ano,vendas ,color ='red')
#     grafico.set_xlabel('ANO')
#     grafico.set_ylabel("VENDAS")


#     #integração inter e matplot
#     canvas = FigureCanvasTkAgg(fig,master=janela)
#     canvas.draw()
#     canvas.get_tk_widget().pack(side = tk.TOP,fill= tk.BOTH, expand = True)

# janela = tk.Tk()
# janela.title("grafico")

# btn = tk.Button(janela, text = "gerar grafico")
# btn.pack(pady = 20)

# janela.mainloop()

import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_data():
    dados =  pd.read_csv('DADOSS.csv')

    ano = dados['Ano']
    vendas =  dados['Vendas']

    fig, grafico = plt.subplots()
    grafico.bar(ano,vendas ,color ='red')
    grafico.set_xlabel('ANO')
    grafico.set_ylabel('VENDAS')
    
    # integração entre tkinter e matplolib
    canvas = FigureCanvasTkAgg(fig,master=janela )
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH, expand = True)


janela  =  tk.Tk()
janela.title('MOSTRAR GRÁFICO')    

btn =  tk.Button(janela, text = 'GERAR GRÁFICO', command = plot_data)
btn.pack(pady = 20)

janela.mainloop()    




