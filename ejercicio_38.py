# 38.- Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica.
#     Reglas:
#         0 - 69: insuficiente
#         70 - 79: bien
#         80 - 89: muy bien
#         90 - 100: excelente

def comprobar_nota(nota):
    if nota < 70:
        return "Insuficiente"
    elif nota < 80:
        return "Bien"
    elif nota < 90:
        return "Muy bien"
    elif nota <= 100:
        return "Excelente"
    else:
        return "Nota no válida"

nota = int(input("Introduce la nota del alumno sobre 100:"))

print(comprobar_nota(nota))