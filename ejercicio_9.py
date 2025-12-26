# 9.- Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter().

def filtar_mascotas(mascotas):
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    mascotas_filtradas = list(filter(lambda x: x not in mascotas_prohibidas, mascotas))
    return mascotas_filtradas

mascotas_candidatas = ["Perro","Mapache","Gato","Tigre","Hámster","Serpiente Pitón","Periquito","Oso","Tortuga"]

print(filtar_mascotas(mascotas_candidatas))