"""System.Module"""

print(
    "Bienvenidos a la calculadora \nPara salir, escribe salir \nLas operaciones permitidas son: suma, multiplicacion, resta y division."
)
while input("") != "salir".lower():
    print("Ingrese el primer numero")
    n1 = int(input())
    print("Ingrese la operacion")
    operacion = input().lower()
    print("Ingrese el segundo numero")
    n2 = int(input())
    if operacion == "suma":
        resultado = n1 + n2
        print("El resultado es: ", resultado)
        break
    elif operacion == "resta":
        resultado = n1 - n2
        print("El resultado es: ", resultado)
    elif operacion == "multiplicacion":
        resultado = n1 * n2
        print("El resultado es: ", resultado)
    elif operacion == "division":
        resultado = n1 / n2
        print("El resultado es: ", resultado)
    else:
        print("no corresponde")
