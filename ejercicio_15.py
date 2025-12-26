# 15.- Crea una función lambda que sume 3 a cada número de una lista dada.

numeros = [1, 2, 3, 4, 5]
sumar_tres = lambda numeros: [numero+3 for numero in numeros]

print(sumar_tres(numeros))