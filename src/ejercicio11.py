################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que indique con True si un número entero
es multiplo de otro, utilizando sumas y restas.
"""
def es_multiplo(numero, multiplo):
    """Esta función recibe dos números enteros positivos y devuelve
    un dato Booleano, siendo True si el primero es múltiplo, y
    False si no lo es."""
    numero = int(numero)
    multiplo = int(multiplo)
    while numero > 0:
        numero = numero - multiplo
    if numero == 0:
        multiplo = True
    else:
        multiplo = False
    return multiplo
def principal():
    """
    Esta función pide ingresar dos números enteros positivos, siendo primero
    el número y luego el que se desea saber si es múltiplo, e imprime una cadena
    de texto indicando si se trata de un múltiplo o no.
    """
    numero = input("Ingrese número: ")
    multiplo = input("Ingrese múltiplo: ")
    input_es_multiplo = es_multiplo(numero, multiplo)
    if input_es_multiplo:
        print(f"{numero} es multiplo de {multiplo}")
    else:
        print(f"{numero} no es múltiplo de {multiplo}")
if __name__ == "__main__":
    principal()
