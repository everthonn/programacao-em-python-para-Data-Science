import statistics

empresas = {
    'empresa 1': [2500, 2800, 3000, 9500, 12000],
    'empresa 2': [5000, 5200, 5300, 5400, 5500],
    'empresa 3': [1000, 2000, 8000, 15000, 20000],
    'empresa 4': [3500, 4000, 4200, 4300, 6000],
    'empresa 5': [1200, 1500, 1800, 2500, 10000]
}

def empresa1(): 
    moda = statistics.mode(empresas['empresa 1'])
    media = statistics.mean(empresas['empresa 1'])
    mediana = statistics.median(empresas['empresa 1'])
    amplitude = max(empresas['empresa 1']) - min(empresas['empresa 1'])
    variancia = statistics.variance(empresas['empresa 1'])
    desvio = statistics.stdev(empresas['empresa 1'])

    print(f"empresa 1 \n Moda {moda} \n Média {media} \n Mediana {mediana} \n Amplitude {amplitude} \n Variância {variancia} \n Desvio {desvio}\n")

def empresa2():
    moda2 = statistics.mode(empresas['empresa 2'])
    media2 = statistics.mean(empresas['empresa 2'])
    mediana2 = statistics.median(empresas['empresa 2'])
    amplitude = max(empresas['empresa 2']) - min(empresas['empresa 2'])
    variancia2 = statistics.variance(empresas['empresa 2'])
    desvio2 = statistics.stdev(empresas['empresa 2'])

    print(f"empresa 2 \n Moda {moda2} \n Média {media2} \n Mediana {mediana2} \n Amplitude {amplitude} \n Variância {variancia2} \n Desvio {desvio2}\n")

def empresa3():
    moda3 = statistics.mode(empresas['empresa 3'])
    media3 = statistics.mean(empresas['empresa 3'])
    mediana3 = statistics.median(empresas['empresa 3'])
    amplitude = max(empresas['empresa 3']) - min(empresas['empresa 3'])
    variancia3 = statistics.variance(empresas['empresa 3'])
    desvio3 = statistics.stdev(empresas['empresa 3'])

    print(f"empresa 3 \n Moda {moda3} \n Média {media3} \n Mediana {mediana3} \n Amplitude {amplitude} \n Variância {variancia3} \n Desvio {desvio3}\n")

def empresa4():
    moda4 = statistics.mode(empresas['empresa 4'])
    media4 = statistics.mean(empresas['empresa 4'])
    mediana4 = statistics.median(empresas['empresa 4'])
    amplitude = max(empresas['empresa 4']) - min(empresas['empresa 4'])
    variancia4 = statistics.variance(empresas['empresa 4'])
    desvio4 = statistics.stdev(empresas['empresa 4'])

    print(f"empresa 4 \n Moda {moda4} \n Média {media4} \n Mediana {mediana4} \n Amplitude {amplitude} \n Variância {variancia4} \n Desvio {desvio4}\n")

def empresa5():
    moda5 = statistics.mode(empresas['empresa 5'])
    media5 = statistics.mean(empresas['empresa 5'])
    mediana5 = statistics.median(empresas['empresa 5'])
    amplitude = max(empresas['empresa 5']) - min(empresas['empresa 5'])
    variancia5 = statistics.variance(empresas['empresa 5'])
    desvio5 = statistics.stdev(empresas['empresa 5'])

    print(f"empresa 5 \n Moda {moda5} \n Média {media5} \n Mediana {mediana5} \n Amplitude {amplitude} \n Variância {variancia5} \n Desvio {desvio5}")

def rankear_empresas(empresas):
    ranking = []
    for nome, salarios in empresas.items():
        moda = statistics.mode(salarios)
        media = statistics.mean(salarios)
        mediana = statistics.median(salarios)
        amplitude = max(salarios) - min(salarios)
        variancia = statistics.variance(salarios)
        desvio = statistics.stdev(salarios)

        score = abs(mediana - (variancia + desvio + amplitude + abs(mediana - moda)))
        ranking.append((nome, score))

    ranking.sort(key=lambda x: x[1])
    print("Um score menor indica maior estabilidade nos salários desta empresa.")
    print("Ranking das empresas:")
    for i, (nome, score) in enumerate(ranking, start=1):
        print(f"{i}º lugar: {nome} com score {score:.3f}")
