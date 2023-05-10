"""PEP8"""

punto = {"x": 25, "y": 50}
print(punto["x"])
print(punto["y"])
punto["z"] = 45

if "a" in punto:
    print("encontre a", punto["a"])

print(punto.get("x"))
print(punto.get("a", 11))
del punto["x"]
del punto["y"]  # lo mismo pero con una funcion

punto["x"] = 25
for valor in punto:
    print(punto[valor])

for valor in punto.items():
    print(valor)  # Devuelve una tupla = llave, valor

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Facundo"},
    {"id": 2, "nombre": "Nicolas"},
    {"id": 3, "nombre": "Franco"},
    {"id": 4, "nombre": "Leila"},
]
for usuario in usuarios:
    print(usuario["nombre"])
