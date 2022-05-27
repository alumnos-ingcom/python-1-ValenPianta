################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas,
obtenga el valor del cociente y resto de dos números enteros.
"""
def division_lenta(dividendo, divisor):
    """Esta función recibe dos numeros enteros y devuelve el cociente y resto
    de dividir el primero por el segundo"""
    divisor = int(divisor)
    dividendo = int(dividendo)
    contador = 0
    while dividendo >= divisor:
        contador += 1
        dividendo = dividendo - divisor
    return (contador, dividendo)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    dividendo = input("Ingrese dividendo: ")
    divisor = input("Ingrese divisor: ")
    resultado = division_lenta(dividendo, divisor)
    cociente = resultado[0]
    resto = resultado[1]
    print(f"El cociente es {cociente} y el resto {resto}")

if __name__ == "__main__":
    principal()
