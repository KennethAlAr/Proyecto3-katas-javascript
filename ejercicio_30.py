# 30.- Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def es_anagrama(palabra_1, palabra_2):
    lista_1 = list()
    lista_2 = list()
    for letra in palabra_1:
        lista_1.append(letra)

    for letra in palabra_2:
        lista_2.append(letra)

    lista_1.sort()
    lista_2.sort()

    if lista_1 == lista_2:
        return "Las dos palabras son anagramas"
    else:
        return "Las dos palabras no son anagramas"
    
palabra_1 = "gato"
palabra_2 = "toga"
palabra_3 = "perro"

print(es_anagrama(palabra_1, palabra_2))
print(es_anagrama(palabra_1, palabra_3))