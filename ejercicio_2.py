# 2.- Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

numeros = [1, 2, 3, 4]

def doblar_numero(numero):
    return numero*2

dobles = list(map(doblar_numero, numeros))

print(dobles)