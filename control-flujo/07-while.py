# numero = 1

# while numero < 100:
#     print(numero)
#     numero *= 2

comando = ""

while True:  # condicion igual a (comando != "salir"):
    comando = input("$ ").lower()
    print(comando)
    if comando.lower() == "salir":
        break
