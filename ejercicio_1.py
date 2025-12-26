# 1.- Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

#El ejercicio no dice nada de los símbolos así que solo tendremos en cuenta las letras
def contador_letras(texto):
    diccionario = dict()
    for letra in texto:
        if letra.isalpha():
            if not letra.lower() in diccionario.keys():
                diccionario[letra] = 1
            else:
                diccionario[letra] += 1
    return diccionario

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
print(contador_letras(texto))