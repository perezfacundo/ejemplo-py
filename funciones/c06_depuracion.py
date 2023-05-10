"""System module"""


def largo(texto):
    resultado = 0
    for _ in texto:
        resultado += 1
    return resultado


print("chanchito")
longitud = largo("Hola Mundo")
print(longitud)
