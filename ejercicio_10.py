# 10.-Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

def media_numeros(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    try:
        media = suma / len(numeros)
    except ZeroDivisionError:
        return "La lista está vacía"
    return media

numeros = [10, 20, 30, 40, 50]
print(media_numeros(numeros))

lista_vacia = []
print(media_numeros(lista_vacia))