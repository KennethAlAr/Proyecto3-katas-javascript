# 36.- Crea una función llamada procesar_texto
#     Procesa un texto según la opción especificada: contar_palabras, reemplazar_palabras o eliminar_palabra.
#     Código a seguir:
#         Crear una función contar_palabras que cuente el número de veces que aparece cada palabra en el texto y devuelva un diccionario.
#         Crear una función reemplazar_palabras para sustituir una palabra_original por una palabra_nueva en el texto y devolver el texto modificado.
#         Crear una función eliminar_palabra que elimine una palabra del texto y devuelva el texto sin ella.
#         Crear la función procesar_texto que reciba un texto, una opción ("contar", "reemplazar", "eliminar") y un número variable de argumentos según la opción   elegida.
#     Caso de uso:
#         Verificar el funcionamiento completo de procesar_texto.

def contar_palabras(texto):
    palabras = texto.split()
    diccionario = dict()
    for palabra in palabras:
        if palabra in diccionario.keys():
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    lista_palabras = texto.split(" ")
    nueva_lista = list(filter(lambda p : p != palabra, lista_palabras))
    return " ".join(nueva_lista)

def procesar_texto(*args):
    match args[0]:
        case "contar":
            return contar_palabras(args[1])
        case "reemplazar":
            return reemplazar_palabras(args[1],args[2],args[3])
        case "eliminar":
            return eliminar_palabra(args[1], args[2])

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"

print(procesar_texto("contar", texto))
print(procesar_texto("reemplazar", texto, "ipsum", "naranja"))
print(procesar_texto("eliminar", texto, "consectetur"))