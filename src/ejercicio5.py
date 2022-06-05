################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que mediante restas sucesivas,
obtenga el valor del cociente y resto de dos números enteros.
"""

def division_lenta(dividendo, divisor):
    """Esta función recibe dos numeros enteros, realiza la división lenta
    y devuelve cociente y resto"""
    cociente = 0
    dividendo = int(dividendo)
    divisor= int(divisor)
    if dividendo > 0 and divisor > 0:
        while dividendo - divisor >= 0:
            cociente += 1
            dividendo -= divisor
    elif dividendo < 0 and divisor < 0:
        while dividendo - divisor <= 0:
            cociente += 1
            dividendo -= divisor
    elif dividendo < 0 and divisor > 0:
        while dividendo + divisor <= 0:
            cociente -= 1
            dividendo += divisor
    elif dividendo > 0 and divisor < 0:
        while dividendo + divisor >= 0:
            cociente -= 1
            dividendo += divisor
    return (cociente, dividendo)

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
