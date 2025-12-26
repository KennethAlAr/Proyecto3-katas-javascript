# 17.- Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().

from functools import reduce

def concatenar_numeros(numero_1, numero_2):
    return int(str(numero_1) + str(numero_2))

numeros = [1,2,3,4]

print(reduce(concatenar_numeros,numeros))