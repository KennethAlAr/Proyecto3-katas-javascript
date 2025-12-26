# 23.- Concatena una lista de palabras. Usa la función reduce().

from functools import reduce

def concatenar_palabras(palabra_1, palabra_2):
    return palabra_1 + palabra_2

palabras = ["¡Hola", " ", "Mundo!", " ", "Mi", " ", "función", " ", "concatena", " ", "palabras."]

print(reduce(concatenar_palabras,palabras))