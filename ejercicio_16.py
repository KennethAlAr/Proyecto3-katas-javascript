# 16.- Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter().

def palabras_mas_largas_que_n(texto, n):
    lista_palabras = texto.split(" ")
    resultado = list(filter(lambda x: len(x) > n, lista_palabras))
    return resultado

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
n = 4

print(palabras_mas_largas_que_n(texto, n))