# 13.- Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map().

def lower_y_upper(palabra):
    resultado = list(set(map(lambda x: (x.lower(), x.upper()), palabra)))
    return resultado

palabra = "Patata"
print(lower_y_upper(palabra))