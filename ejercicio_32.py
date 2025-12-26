# 32.- Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.

def buscar_empleado(nombre, empleados):
    for empleado in empleados:
        if nombre == empleado["nombre"]:
            return f"{nombre} trabaja aquí y su puesto es {empleado["puesto"]}."
    return f"{nombre} no trabaja aquí."

empleados = [
    {"nombre": "Juan Pérez", "puesto": "Analista de Datos"},
    {"nombre": "María García", "puesto": "Desarrolladora Backend"},
    {"nombre": "Carlos Rodríguez", "puesto": "Gerente de Proyectos"},
    {"nombre": "Ana Martínez", "puesto": "Diseñadora UX"},
    {"nombre": "Laura Sánchez", "puesto": "Especialista en Marketing"}
]

nombre_1 = "Carlos Rodríguez"
nombre_2 = "Pedro Domínguez"

print(buscar_empleado(nombre_1, empleados))
print(buscar_empleado(nombre_2, empleados))