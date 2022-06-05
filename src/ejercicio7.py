################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir un programa que permita transformar un número solicitado expresado en grados, minutos y segundos
a segundos a segundos. Y otra que haga el cambio en el sentido contrario,
devolviendo una tuple
"""
def sexadecimal_a_decimal(horas, minutos, segundos):
    """Esta función recibe tres números enteros positivos (horas, minutos y segundos),
    y devuelve un número entero que representa la cantidad de segundos."""
    horas = int(horas)
    minutos = int(minutos)
    segundos = int(segundos)
    minutos += horas * 60
    segundos += minutos * 60
    return segundos
def decimal_a_sexadecimal(numero):
    """Esta función recibe un número entero positivo que representa los segundos y
    devuelve una tupla de tres números enteros positivos, representando el equivalente
    en horas, minutos y segundos."""
    numero = int(numero)
    lista = []
    horas = numero // 3600
    minutos = numero // 60 - 60 * horas
    segundos = numero - 60 * minutos - 3600 * horas
    lista.append(horas)
    lista.append(minutos)
    lista.append(segundos)
    return tuple(lista)
def principal():
    """
    Esta función pide introducir tres números enteros positivos por consola que representan
    horas, minutos y segundos, e imprime su equivalente en un numero entero que representa
    los segundos.
    Luego pide introducir los segundos como un numero entero positivo, e imprime su
    equivalente en horas, minutos y segundos.
    """
    horas = input("Ingrese horas: ")
    minutos = input("Ingrese minutos: ")
    segundos = input("Ingrese segundos: ")
    a_segundos = sexadecimal_a_decimal(horas, minutos, segundos)
    print(f"{horas} horas, {minutos} minutos, y {segundos} segundos son {a_segundos} segundos.")
    numero = input("Ingrese segundos para convertir a horas, minutos y segundos: ")
    a_horas = decimal_a_sexadecimal(numero)
    print(f"{numero} segundos son {a_horas[0]} horas, {a_horas[1]} minutos y {a_horas[2]} segundos.")
if __name__ == "__main__":
    principal()
