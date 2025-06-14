import statistics

def moda(produtos):
    return statistics.mode(produtos)

def media(produtos):
    return statistics.mean(produtos)  
def mediana(produtos):
    return statistics.median(produtos)

def amplitude(produtos):
    return max(produtos) - min(produtos)

def variancia(produtos):
    return statistics.variance(produtos)

def desvio(produtos):
    return statistics.stdev(produtos)  