import numpy as np
from sklearn.linear_model import LinearRegression

vendas = {
    'JULHO' : 500000,

    'AGOSTO' : 700000,

    'SETEMBRO' : 900000,

    'OUTUBRO' : 90000,

    'NOVEMBRO' : 1000000
}

meses = np.array([vendas.keys()]).reshape(-1,1)

print(meses)