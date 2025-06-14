import numpy as np
import timeit

matrizfeia = [1,2,3,3,4,4,5,65,54,12]


# soma max min 
soma = np.sum(matrizfeia)
maximo = np.max(matrizfeia)
minimo = np.min(matrizfeia)

# media moda mediana
media = np.mean(matrizfeia)
mediana = np.median(matrizfeia)
# moda = np.mode(matrizfeia)
print(media, mediana)
