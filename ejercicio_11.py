# 11.- Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def comprobar_edad(edad):
    try:
        if int(edad) < 0:
            return "No puedes tener menos de 0 años."
        elif int(edad) > 120:
            return "No puedes tener mas de 120 años."
        else:
            return f"Tienes {edad} años."
    except ValueError:
        return "Introduce una edad válida."

edad = input("Introduce tu edad")
print(comprobar_edad(edad))