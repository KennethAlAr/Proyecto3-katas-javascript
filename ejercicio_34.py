# 34.- Crea la clase Arbol:
#     Define un árbol genérico con un tronco y ramas como atributos.
#     Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
#     Código a seguir:
#         Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
#         Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
#         Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
#         Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
#         Implementar el método quitar_rama para eliminar una rama en una posición específica.
#         Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
#     Caso de uso:
#         a. Crear un árbol.
#         b. Hacer crecer el tronco una unidad.
#         c. Añadir una nueva rama.
#         d. Hacer crecer todas las ramas una unidad.
#         e. Añadir dos nuevas ramas.
#         f. Retirar la rama situada en la posición 2.
#         g. Obtener información sobre el árbol.

class Arbol():
    def __init__(self):
        self.tronco = 1
        self.ramas = list()
    
    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama+1 for rama in self.ramas]
    
    def quitar_rama(self, posicion):
        self.ramas.pop(posicion)

    def informacion_arbol(self):
        print(f'''Longitud del tronco: {self.tronco} metros.
Número de ramas: {len(self.ramas)} ramas.
Longitudes de ramas: {self.ramas}''')

roble = Arbol()
roble.crecer_tronco()
roble.nueva_rama()
roble.crecer_ramas()
roble.nueva_rama()
roble.nueva_rama()
roble.quitar_rama(2)
roble.informacion_arbol()