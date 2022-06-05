################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""
def compara(numero, otro_numero):
    """Esta función recibe dos números y devuelve
    -1 si el primero es menor
    0 si son iguales
    1 si el primero es mayor"""
    numero = int(numero)
    otro_numero = int(otro_numero)
    if numero - otro_numero > 0:
        comparacion = 1
    elif numero - otro_numero < 0:
        comparacion = -1
    else:
        comparacion = 0
    return comparacion
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    primer_num = input("Ingrese primer número: ")
    segundo_num = input("Ingrese segundo número: ")
    comparar = compara(primer_num, segundo_num)
    print(comparar)
if __name__ == "__main__":
    principal()
