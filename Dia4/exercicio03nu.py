import numpy as np


vendas = np.array([120, 90, 150, 80, 200, 110, 50, 300])

vendas_maiores_100 = vendas[vendas > 100]
print("Vendas maiores que 100:", vendas_maiores_100)

media_vendas = np.mean(vendas)
vendas_abaixo_media = vendas[vendas < media_vendas]
print("Quantidade de vendas abaixo da média:", len(vendas_abaixo_media))

vendas_normalizadas = vendas / np.max(vendas)    
print("Vendas normalizadas:", vendas_normalizadas)