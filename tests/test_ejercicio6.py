################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor
"""
Este es el test correspondiente al archivo 'ejercicio6.py'
"""

def test_ordenar_mayor_a_menor():
    """Caso de prueba de la función ordenar_mayor_a_menor"""
    numero = 1
    segundo_numero = 3
    tercer_numero = 5
    resultado = ordenar_mayor_a_menor(numero, segundo_numero, tercer_numero)
    assert isinstance(resultado[0], int), "El resultado 0 debe ser un número entero"
    assert isinstance(resultado[1], int), "El resultado 1 debe ser un número entero"
    assert isinstance(resultado[2], int), "El resultado 2 debe ser un número entero"
    assert resultado == (5, 3, 1), "El resultado no es el esperado"
    
def test_ordenar_menor_a_mayor():
    """Caso de prueba de la función ordenar_menor_a_mayor"""
    numero = 12
    segundo_numero = 4
    tercer_numero = 28
    resultado = ordenar_menor_a_mayor(numero, segundo_numero, tercer_numero)
    assert isinstance(resultado[0], int), "El resultado 0 debe ser un número entero"
    assert isinstance(resultado[1], int), "El resultado 1 debe ser un número entero"
    assert isinstance(resultado[2], int), "El resultado 2 debe ser un número entero"
    assert resultado == (4, 12, 28), "El resultado no es el esperado"