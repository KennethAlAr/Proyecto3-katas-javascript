# 33.- Crea una función lambda que sume elementos correspondientes de dos listas dadas.

lista_1 = [1,2,3,4]
lista_2 = [4,3,2,1]

suma = lambda lista_x, lista_y: list(map(lambda x, y: x + y, lista_x, lista_y))

print(suma(lista_1, lista_2))