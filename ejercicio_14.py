# 14.- Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter().

def comienza_por(palabras, letra):
    palabras_filtradas = list(filter(lambda x: x[0].lower() == letra.lower(), palabras))
    return palabras_filtradas

palabras = ["Arbol","avión","Banana","Ana","Casa","Elefante"]
print(comienza_por(palabras, "a"))