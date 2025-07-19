import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


dados = pd.read_csv('./Dia8/atividadeFinal/dados.csv')
df = pd.DataFrame(dados)

X = np.array(df.index).reshape(-1,1)
y = np.array(df['Tempo_espera'])

modelo = LinearRegression()
modelo.fit(X,y)

previsao = modelo.predict([[len(df)+1]])

print(f'PREVISÃO DE TEMPO DE ESPERA PARA PROXIMO PASCIENTE {previsao}')