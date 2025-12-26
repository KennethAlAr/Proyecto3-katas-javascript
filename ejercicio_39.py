# 39.- Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos necesarios para calcular el área de la figura).

from math import pi

def calcular_area(figura, datos):
    match figura:
        case "rectangulo":
            return datos[0] * datos[1]
        case "circulo":
            return pi * (datos[0] ** 2)
        case "triangulo":
            return datos[0] * datos[1] / 2

print(calcular_area("rectangulo", (4,2)))
print(calcular_area("circulo", (3,)))
print(calcular_area("rectangulo", (3,3)))