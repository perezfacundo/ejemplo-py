"""System.Module"""


def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 6)
suma(4, 6)
suma(5, 234, 4234, 7)
