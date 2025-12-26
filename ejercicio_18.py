# 18.- Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90.

alumnos = [
    {"nombre": "Ana García", "edad": 20, "calificación": 95},
    {"nombre": "Luis Pérez", "edad": 22, "calificación": 88},
    {"nombre": "Marta Sanz", "edad": 19, "calificación": 90},
    {"nombre": "Javier López", "edad": 21, "calificación": 75},
    {"nombre": "Lucía Fernández", "edad": 20, "calificación": 92},
    {"nombre": "Diego Ruiz", "edad": 23, "calificación": 89},
    {"nombre": "Elena Gómez", "edad": 19, "calificación": 98}
]

print(list(filter(lambda x: x["calificación"] >= 90, alumnos)))