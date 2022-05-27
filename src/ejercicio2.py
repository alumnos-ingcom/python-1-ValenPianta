################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que reciba un número e indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.
"""

def signo(numero):
    """ Función que recibe un múmero e indica si es positivo,
    negativo o cero. """
    numero = float(numero)
    if numero + numero > numero:
        su_signo = 1
    elif numero + numero < numero:
        su_signo = -1
    else:
        su_signo = 0
    return su_signo

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = input("Ingrese número: ")
    signo_del_num = signo(numero)
    if signo_del_num == -1:
        signo_ingresado = "es negativo"
    elif signo_del_num == 1:
        signo_ingresado = "es positivo"
    else:
        signo_ingresado = "es cero"
    print(f"El numero ingresado {signo_ingresado}")

if __name__ == "__main__":
    principal()
