import modulo


lista =  [1,2,4,5,360]
lista.sort()
print(lista)
media_ = modulo.media(lista)
print('media', media_)


moda = modulo.moda(lista)
print('Moda:', moda)

med = modulo.mediana(lista)
print('Mediana', med)

