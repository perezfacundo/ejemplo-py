"""PEP8"""

numeros = [1, 5, 2, 6, 8, 3, 1, 5, 7]

numeros.sort()
numeros.sort(reverse=True)  # modifica el orden de la lista

numerosOrdenados = sorted(
    numeros, reverse=True  # o False
)  # Crea una nueva lista sin modificar el orden de la original

print(numeros)

usuarios = [["Panchito", 5], ["Felipe", 7], ["Pulga", 1]]


def ordena(elemento):
    """Ordena"""
    return elemento[1]


usuarios.sort(
    key=lambda el: el[1]
)  # parametro:valor que debe devolver (lambda func anonima)

print(usuarios)
