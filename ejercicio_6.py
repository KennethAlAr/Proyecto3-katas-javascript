# 6.- Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(numero):
    if numero > 1:
        resultado = numero * factorial(numero-1)
        return resultado
    else:
        return numero
    
print(factorial(5))