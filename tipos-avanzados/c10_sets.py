"""PEP8"""

# "set" significa grupo o conjunto
primerSet = {1, 1, 2, 2, 3, 4}  # print: {1, 2, 3, 4} no muestra duplicados
primeraLista = [3, 4, 5]
segundoSet = set(primeraLista)

# Relaciones logicas entre dos o mas conjuntos de elementos
print(primerSet | segundoSet)  # |: Operador Union : {1,2,3,4,5}
print(primerSet & segundoSet)  # &: Operador Interseccion: {3,4}
print(primerSet - segundoSet)  # -: Operador Diferencia: {1,2}
print(primerSet ^ segundoSet)  # ^: Operador Diferencia simetrica: {1,2,5}
