################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Enunciado del ejercicio
"""
def es_primo(numero):
    """ Esta función recibe un numero entero y devuelve si es verdadero o no,
    de forma Booleana, siendo True que es primo, y False que no es primo."""
    primo = True
    numero = int(numero)
    for n in range(2, numero):
        if numero % n == 0:
            primo = False
    if numero == 1:
        primo = False
    return primo

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = input("Ingrese número: ")
    numero_es_primo = es_primo(numero)
    if numero_es_primo:
        print("Es primo!")
    else:
        print("No es primo")

if __name__ == "__main__":
    principal()
