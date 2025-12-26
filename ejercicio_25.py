# 25.- Crea una función que cuente el número de caracteres en una cadena de texto dada.

from functools import reduce

texto = input("Introduce un texto:")

resultado = reduce(lambda i, x: i+1, texto, 0)

print(resultado)

print(len(texto))