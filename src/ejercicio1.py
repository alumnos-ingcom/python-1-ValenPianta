################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit
como un número decimal, utilice esta formula para calcular los grados centígrados y retorne
el resultado obtenido. Y viceversa.
"""

def convertir_a_fahrrenheit(centigrados):
    """Esta función transforma una temperatura en grados centígrados
    a grados fahrenheit"""
    conversion = float(centigrados) * 1.8 + 32
    redondeado = round(conversion, 2)
    return redondeado
def convertir_a_centigrados(fahrenheit):
    """Esta función transforma una temperatura en grados fahrenheit
    a grados centígrados"""
    conversion = (float(fahrenheit) -32) / 1.8
    redondeado = round(conversion, 2)
    return redondeado
def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    grados_c = input("Ingrese grados centígrados para convertir a fahrenheit: ")
    cent_a_fahr = convertir_a_fahrrenheit(grados_c)
    print(f"{grados_c} grados centígrados son {cent_a_fahr} grados fahrenheit.")
    grados_f = input("Ingrese grados fahrenheit para convertir a centígrados: ")
    fahr_a_cent = convertir_a_centigrados(grados_f)
    print(f"{grados_f} grados fahrenheit son {fahr_a_cent} grados centígrados.")
if __name__ == "__main__":
    principal()
