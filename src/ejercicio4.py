################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que haga la suma entre dos números enteros
sin hacer la operación de manera directa.
Esto quiere decir que para hacer la suma entre 4 y 3,
las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""
def suma_lenta(numero, otro_numero):
    """Esta función recibe dos números enteros y realiza la suma lenta"""
    suma = int(numero)
    otro_numero = int(otro_numero)
    for n in range(otro_numero):
        suma += 1
    return suma
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero_uno = input("Ingrese primer número: ")
    numero_dos = input("Ingrese segundo número: ")
    resultado = suma_lenta(numero_uno, numero_dos)
    print(f"El resultado es {resultado}")
if __name__ == "__main__":
    principal()
