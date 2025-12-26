# 20.- Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().

elementos_mixtos = [42, "hola", 10, "Python", 7, "33", -5, "mundo", 0, "True"]

solo_int = list(filter(lambda x: type(x) == int, elementos_mixtos))

print(solo_int)