# 12.- Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map().

def contar_letras_palabra(texto):
    lista_palabras = texto.split()
    resultado = list(map(len, lista_palabras))
    return resultado

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
print(contar_letras_palabra(texto))