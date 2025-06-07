import statistics

FREQUENCIA1 = [2,3,3,1,2,3,3,3,3,6,5,5,5,4]
FREQUENCIA2 = [1.5,6.8,9.7,10.6]
FREQUENCIA3 = [200,300,200,200,500,900,700,900,400,600]

FREQUENCIA3.sort()
print("Lista ordenada:", FREQUENCIA3)

elementos_unicos = set(FREQUENCIA3)
max_vezes = 0
elemento_mais_frequente = None

for elemento in elementos_unicos:
    vezes = FREQUENCIA3.count(elemento)
    if vezes > max_vezes:
        max_vezes = vezes
        elemento_mais_frequente = elemento

print(f"Elemento mais frequente: {elemento_mais_frequente} ({max_vezes} vezes)")


amplitude = max(FREQUENCIA1) - min(FREQUENCIA1)
print(amplitude)

variancia = statistics.variance(FREQUENCIA1)
print(variancia)



























# FREQUENCIA1  =  [1,1,1,2,3,3,3,3,6,5,5,5,4]

# FREQUENCIA2  =  [1.5,6.8,9.7,10.6]

# FREQUENCIA3  =  [200,300,500,700,900,400,600]
# indice2 = 1

# for m in range(2):
#     for i in range(len(FREQUENCIA1)):
#         vezes = 0
#         indice = 0
#         vezes2 = 0
    
#         FREQUENCIA1.sort()
#         if FREQUENCIA1[i] == FREQUENCIA1[indice]:
#             vezes += 1
#         for r in range(len(FREQUENCIA1)):
            
        
#             if FREQUENCIA1[r] == FREQUENCIA1[indice2]:
#                 vezes2 += 1
#         indice2 += 1
#     print(vezes,vezes2)


# print (vezes)
    
    
        
        















        # for r in range(FREQUENCIA1):
    #     if FREQUENCIA1[i] == FREQUENCIA1[r]:
    #         vezes += 1 