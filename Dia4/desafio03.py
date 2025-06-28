from funcoes_desafio03 import *



produtos = {
    'celular':2400,
    'notebook': 5000,
    'tablet': 1500,
    'smartwatch': 800,
    'fones de ouvido': 400,
    'smart speaker': 300,
    'smart TV': 2500,
    'console de videogame': 3000,
    'câmera digital': 1200,
    'impressora': 600,
    'monitor': 900,
    'teclado mecânico': 200,
    'mouse gamer': 150,
    'pendrive': 100,
    'HD externo': 400,
    'SSD': 800,
    'router': 250,
    'webcam': 200,
    'microfone': 300,
    'projetor': 1500,
    'scanner': 700,
    'smartphone dobrável': 8000,
    'smartphone com câmera tripla': 5000,
    'notebook gamer': 12000,
    'smartwatch com monitor de saúde': 1500,
    'fones de ouvido com cancelamento de ruído': 1000,
    'controle de videogame sem fio': 300,
    'controle remoto universal': 100,
    'carregador portátil': 200,
    'cabo HDMI': 50,
    'suporte para notebook': 150
}
precos = list(produtos.values())
valores = []

for i,(chave, valor) in enumerate(produtos.items()):
    print(f"Produto: {chave} \nPreço: R${valor:.2f} \n")
    valores.append(valor)

print(f'moda {moda(valores)}')
print(f'média {media(valores)}')
print(f'mediana {mediana(valores)}')
print(f'amplitude {amplitude(valores)}')
print(f'variância {variancia(valores)}')
print(f'desvio {desvio(valores)}')








