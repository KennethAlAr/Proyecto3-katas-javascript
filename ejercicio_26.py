# 26.- Crea una función lambda que calcule el resto de la división entre dos números dados.

numero_1 = int(input("Escribe un número:"))
numero_2 = int(input("Escribe otro número:"))

resto = lambda x, y: x % y

print(f"El resto de dividir {numero_1} entre {numero_2} es: {resto(numero_1, numero_2)}")