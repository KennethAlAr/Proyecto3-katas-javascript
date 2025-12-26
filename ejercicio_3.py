# 3.- Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

def buscar_palabra(palabras, objetivo):
    resultado = list()
    for palabra in palabras:
        if objetivo.lower() in palabra.lower():
            resultado.append(palabra)
    return set(resultado)

palabras = lista_palabras = ["sol","girasol","soldado","absoluto","luna","parasol","soledad","mar","consolar"]
print(buscar_palabra(palabras, "sol"))