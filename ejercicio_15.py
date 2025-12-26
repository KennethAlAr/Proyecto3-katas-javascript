# 15.- Crea una función lambda que sume 3 a cada número de una lista dada.

numeros = [1, 2, 3, 4, 5]
sumar_tres = list(map(lambda x: x+3, numeros))

print(sumar_tres)