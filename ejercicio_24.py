# 24.- Calcula la diferencia total en los valores de una lista. Usa la función reduce().

from functools import reduce

def diferencia_valores(numero_1, numero_2):
    return numero_1 - numero_2

numeros = [100, 20, 10, 5]

print(reduce(diferencia_valores,numeros))