"""PEP8"""

# DESEMPAQUETAMIENTO CON LISTAS
lista1 = [1, 2, 3, 4]
# print(1, 2, 3, 4)
# print(*lista)

lista2 = [5, 6]
combinada = [
    "Hola ",
    *lista1,
    " mundo",
    *lista2,
    "chanchito",
]  # con el * como operador de desenpaquetamiento
print(combinada)

# DESEMPAQUETAMIENTO CON TUPLAS
punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)
