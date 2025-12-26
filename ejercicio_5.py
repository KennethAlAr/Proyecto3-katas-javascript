# 5.- Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será "aprobado"; de lo contrario, "suspenso". La función debe devolver una tupla que contenga la media y el estado.

def media_aprobada(notas, nota_aprobado=5):
    suma = 0
    for numero in notas:
        suma += numero
    media = suma / len(notas)
    if media >= nota_aprobado:
        return (media, "aprobado")
    else:
        return (media, "suspenso")
    
notas_1 = [7, 8, 6, 9, 10]
print(media_aprobada(notas_1))

notas_2 = [3, 4, 2, 5, 1]
print(media_aprobada(notas_2))

notas_3 = [6, 6, 6, 6]
print(media_aprobada(notas_3, 7))