# 29.- Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.

def enmascarar_texto(texto):
    texto = str(texto)
    nuevo_texto = ""
    for i in range(len(texto)):
        if i < len(texto) - 4:
            nuevo_texto += "#"
        else:
            nuevo_texto += texto[i]
    return nuevo_texto

texto = 12345678

print(enmascarar_texto(texto))