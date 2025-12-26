# 28.- Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def buscar_primer_duplicado(lista):
    control = list()
    for elemento in lista:
        if elemento not in control:
            control.append(elemento)
        else:
            return elemento
        
lista = [1,2,3,4,4,5,6,6,7,7,8,9,4]

print(buscar_primer_duplicado(lista))