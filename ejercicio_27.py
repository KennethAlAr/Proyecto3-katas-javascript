# 27.- Crea una función que calcule el promedio de una lista de números.

from functools import reduce

numeros = [1,2,3,4,5,6]

resultado = (reduce(lambda x, y: x+y, numeros))/len(numeros)

print(resultado)