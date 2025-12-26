# 7.- Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

def convertir_a_lista_strings(lista_tuplas):
    lista = list(map(lambda x: " ".join(x), lista_tuplas))
    return lista

tuplas = [
    ("Hola", "Mundo"),
    ("Uno", "Dos", "Tres", "Cuatro"),
    ("Solito",),
    ("Clave", "Valor")
]

print(convertir_a_lista_strings(tuplas))