################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne una tuple con
factores primos de un numero entero positivo.
"""
def factores_primos(numero):
    """Esta función recibe un numero entero positivo y retorna
    una tupla con los sus factores primos"""
    numero = int(numero)
    lista = []
    contador = 2
    while numero > 1:
        if numero % contador == 0:
            lista.append(contador)
            numero = numero // contador
        else:
            contador += 1
    return tuple(lista)
def principal():
    """
    Esta función solicita por consola un numero entero positivo e imprime
    sus factores primos.
    """
    valor = input("Ingrese numero para calcular factores primos: ")
    factores_p = factores_primos(valor)
    print(f"Los factores primos de {valor} son {factores_p}")

if __name__ == "__main__":
    principal()
