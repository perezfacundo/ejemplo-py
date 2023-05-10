"""System module"""


def no_space(texto):
    """Funcion que quita espacios de un string"""
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            char = buscar(char)
            nuevo_texto += char
    print(nuevo_texto)
    return nuevo_texto


def buscar(letra):
    """Esta funcion quita las tildes de cada letra"""
    letras = [
        ["a", "á"],
        ["e", "é"],
        ["i", "í"],
        ["o", "ó"],
        ["u", "ú"],
    ]
    #buscar la letra con la tilde y devolver la letra sin tilde
    for renglon in letras:
        letra == letras[][]
    return letra


# Cambia la letra pero se puede mejorar
# for ct, st in reemplazos:
#     print(letra)
#     letra = letra.replace(ct, st)
#     print(letra)


def reverse(texto):
    """Da vuelta el string"""
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    print(texto_al_reves)
    return texto_al_reves


def es_palindromo(texto):
    """Verifica si es palindromo"""
    texto_sin_espacios = no_space(texto)
    texto_al_reves = reverse(texto_sin_espacios)
    print(texto_sin_espacios, texto_al_reves)
    if texto_sin_espacios.lower() == texto_al_reves.lower():
        return True
    else:
        return False


print(es_palindromo("Dábale arroz a la zorra el abad"))
