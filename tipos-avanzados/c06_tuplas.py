"""PEP8"""

numeros = (
    1,
    2,
    3,
    23523,
    45,
    636,
    434,
    5,
    65,
)

# Usar tuplas cuando no se quiera modificar accidentalmente un listado

punto = tuple([1, 2, 235, 3463, 46])
print(punto)
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros  # Operador de desenpaquetamiento
print(primero, segundo, otros)

for n in numeros:
    print(n)
# numeros[0] = 0 #Da error porque las tuplas no se pueden modificar

listaNumeros = list(
    numeros
)  # Pero si se puede crear una lista copiando la tupla y modificar la lista
listaNumeros[0] = "Chanchi"
print(listaNumeros)
