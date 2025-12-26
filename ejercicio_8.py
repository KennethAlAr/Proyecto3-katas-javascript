# 8.- Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.

def dividir_numeros(numero_1, numero_2):
    try:
        resultado = float(numero_1) / float(numero_2)
        return f"El resultado de dividir {numero_1} y {numero_2} es: {resultado}"
    except ValueError:
        return "El numerador o el denominador no eran números válidos"
    except ZeroDivisionError:
        return "No se puede dividir entre cero"
    
numero_1 = input("Escribe el numerador de la división:")
numero_2 = input("Escribe el denominador de la división:")
    
print(dividir_numeros(numero_1, numero_2))