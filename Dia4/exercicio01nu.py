import numpy as np

ar = np.array([1, 2, 3, 4, 5])

multiplicado = ar * 10
print("Array multiplicado por 10:", multiplicado)


media = np.mean(ar)
print("Média dos valores:", media)

ar_pares_substituidos = ar.copy()
ar_pares_substituidos[ar_pares_substituidos % 2 == 0] = -1
print("Array com pares substituídos por -1:", ar_pares_substituidos)