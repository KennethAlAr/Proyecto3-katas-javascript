# 22.- Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce().

from functools import reduce

def producto_numeros(numero_1, numero_2):
    return numero_1 * numero_2

numeros = [1,2,3,4]

print(reduce(producto_numeros,numeros))