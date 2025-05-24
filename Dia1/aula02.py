lista = [100,20,3,4,5,6]
lista_teste = lista.copy()
print(lista_teste)

# ordenar

lista_teste.sort(reverse=True)
print(lista_teste)
lista_teste.sort()
print(lista_teste)

# contagem

contagem = lista_teste.count(100)
print(contagem)

# comprimento

comprimento = len(lista)
print(comprimento)

# posição

posicao = lista_teste.index(5)
print(posicao)

# menor valor 

minimo = min(lista_teste)
print(minimo)

# maior valor 

maximo = max(lista_teste)
print(maximo)