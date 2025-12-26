# 4.- Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

def restar_listas(lista_1, lista_2):
    resultado = list(map(lambda x, y: x-y, lista_1, lista_2))
    return resultado

lista_1 = [5,6,7,8,9]
lista_2 = [1,2,3,4,5]
print(restar_listas(lista_1, lista_2))