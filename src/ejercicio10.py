################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si una palabra o frase
ingresada se trata de un palindromo. Palíndromo, es si se lee igual
de derecha a izquierda que de izquierda a derecha."""
def es_palindromo(texto):
    """Esta función recibe una cadena de texto y devuelve un valor Booleano,
    siendo True si el texto ingresado es un palíndromo, y False si no lo es."""
    texto_invertido = ""
    for l in texto:
        texto_invertido = l + texto_invertido
    if texto == texto_invertido:
        texto_es_palindromo = True
    else:
        texto_es_palindromo = False
    return texto_es_palindromo

def principal():
    """
    Esta función pide ingresar una cadena de texto e imprime otra cadena de
    texto indicando si la ingresada se trata de un palíndromo o no.
    """
    entrada = input("Ingrese texto: ")
    es_un_palindromo = es_palindromo(entrada)
    if es_un_palindromo:
        print("Se trata de un palíndromo")
    else:
        print("No se trata de un palíndromo")

if __name__ == "__main__":
    principal()
