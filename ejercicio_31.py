# 31.- Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción.

def buscar_en_lista():
    nombres = list()
    nombre = ""
    while nombre != "salir":
        nombre = input("Escribe un nombre para añadir a la lista o 'salir' para terminar:")
        if nombre != "salir":
            nombres.append(nombre)
    buscado = input("Escribe el nombre que quieres buscar en la lista:")
    if buscado in nombres:
        return f"El nombre '{buscado}' está en la lista."
    else:
        raise Exception (f"El nombre '{buscado}' no está en la lista.")

try:
    print(buscar_en_lista())
except Exception as e:
    print(e)