import statistics
import modulo


empresa1 = [2500, 2800, 3000, 9500, 12000]

empresa2 = [5000, 5200, 5300, 5400, 5500]

empresa3 = [1000, 2000, 8000, 15000, 20000]

empresa4 = [3500, 4000, 4200, 4300, 6000]

empresa5 = [1200, 1500, 1800, 2500, 10000]

moda = statistics.mode(empresa1)
moda2 = statistics.mode(empresa2)
moda3 = statistics.mode(empresa3)
moda4 = statistics.mode(empresa4)
moda5 = statistics.mode(empresa5)

media = statistics.median(empresa1)
media2 = statistics.median(empresa2)
media3 = statistics.median(empresa3)
media4 = statistics.median(empresa4)
media5 = statistics.median(empresa5)

variancia = statistics.variance(empresa1)
variancia2 = statistics.variance(empresa2)
variancia3 = statistics.variance(empresa3)
variancia4 = statistics.variance(empresa4)
variancia5 = statistics.variance(empresa5)

desvio = statistics.stdev(empresa1)
desvio2 = statistics.stdev(empresa2)
desvio3 = statistics.stdev(empresa3)
desvio4 = statistics.stdev(empresa4)
desvio5 = statistics.stdev(empresa5)


print("//////////////////////////////////////////")

print(moda)
print(moda2)
print(moda3)
print(moda4)
print(moda5)


print("//////////////////////////////////////////")

print(media)
print(media2)
print(media3)
print(media4)
print(media5)

print("//////////////////////////////////////////")

print(variancia)
print(variancia2)
print(variancia3)
print(variancia4)
print(variancia5)

print("//////////////////////////////////////////")

print(desvio)
print(desvio2)
print(desvio3)
print(desvio4)
print(desvio5)