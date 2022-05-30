################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que a partir de tres variables de tipo entero
retorne una tupla con dichos valores ordenados de menor a mayor.
Y Viceversa
"""
def ordenar_mayor_a_menor(uno, dos, tres):
    """Función que recibe tres numeros enteros
    y devuelve una tupla con los mismos ordenados
    de mayor a menor"""
    lista = []
    uno = int(uno)
    dos = int(dos)
    tres = int(tres)
    if uno > dos and uno > tres:
        lista.append(uno)
        if dos > tres:
            lista.append(dos)
            lista.append(tres)
        else:
            lista.append(tres)
            lista.append(dos)
    elif dos > uno and dos > tres:
        lista.append(dos)
        if uno > tres:
            lista.append(uno)
            lista.append(tres)
        else:
            lista.append(tres)
            lista.append(uno)
    else:
        lista.append(tres)
        if uno > dos:
            lista.append(uno)
            lista.append(dos)
        else:
            lista.append(dos)
            lista.append(uno)
    return tuple(lista)
def ordenar_menor_a_mayor(uno, dos, tres):
    """Función que recibe tres numeros enteros
    y devuelve una tupla con los mismos ordenados
    de menor a mayor"""
    lista = []
    uno = int(uno)
    dos = int(dos)
    tres = int(tres)
    if uno < dos and uno < tres:
        lista.append(uno)
        if dos < tres:
            lista.append(dos)
            lista.append(tres)
        else:
            lista.append(tres)
            lista.append(dos)
    elif dos < uno and dos < tres:
        lista.append(dos)
        if uno < tres:
            lista.append(uno)
            lista.append(tres)
        else:
            lista.append(tres)
            lista.append(uno)
    else:
        lista.append(tres)
        if uno < dos:
            lista.append(uno)
            lista.append(dos)
        else:
            lista.append(dos)
            lista.append(uno)
    return tuple(lista)
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    uno = input("Ingrese primer número: ")
    dos = input("Ingrese segundo número: ")
    tres = input("Ingrese tercer número: ")
    mayor_primero = ordenar_mayor_a_menor(uno, dos, tres)
    menor_primero = ordenar_menor_a_mayor(uno, dos, tres)
    print(f"De mayor a menor son {mayor_primero}")
    print(f"De menor a mayor son {menor_primero}")

if __name__ == "__main__":
    principal()
