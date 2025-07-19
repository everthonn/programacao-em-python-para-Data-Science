import numpy as np
from sklearn.linear_model import LinearRegression

vendas = {
    'JULHO' : 500000,

    'AGOSTO' : 700000,

    'SETEMBRO' : 900000,

    'OUTUBRO' : 90000,

    'NOVEMBRO' : 1000000
}

nomes_lista = list(vendas.keys())
meses_em_numeros = [i + 1 for i in range(len(nomes_lista))]

meses = np.array(meses_em_numeros).reshape(-1,1)
valores = list(vendas.values())

modelo = LinearRegression()

modelo.fit(meses, valores)


proximo_mes = len(meses_em_numeros) + 1
venda_prevista = modelo.predict([[proximo_mes]])[0]

print(f'Previsão de venda para o proximo mês - {proximo_mes} -> {venda_prevista}')