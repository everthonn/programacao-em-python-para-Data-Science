import numpy as np

matriz = np.random.randint(0, 101, size=(5, 5))
print("Matriz 5x5:\n", matriz)

medias_linhas = np.mean(matriz, axis=1)
print("Média de cada linha:", medias_linhas)

valor_maximo = np.max(matriz)
valor_minimo = np.min(matriz)
print("Valor máximo da matriz:", valor_maximo)
print("Valor mínimo da matriz:", valor_minimo)