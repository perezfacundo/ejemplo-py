"""PEP8"""

usuarios = [["Panchito", 5], ["Felipe", 7], ["Pulga", 1]]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres) = ['Panchito', 'Felipe', 'Pulga']

# TRANSFORMACION (lo mismo pero simplificado) o .map()
# nombres = [usuario[0] for usuario in usuarios]
# print(nombres)

# FILTRADO (saco de la lista lo que me interesa) o .filter()
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombres)

# TRANSFORMACION Y FILTRADO
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
# print(nombres)  # Panchito y Felipe

# TRANSFORMACION con expresion lambda o anonima
# nombres = list(map(lambda usuario: usuario[0], usuarios))
# print(nombres)

# FILTRADO con expresion lambda o anonima
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
