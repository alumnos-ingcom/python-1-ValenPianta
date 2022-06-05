################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal
"""
Este es el test correspondiente al archivo 'ejercicio7.py'
"""

def test_sexadecimal_a_decimal():
    """Caso de prueba de la función sexadecimal_a_decimal"""
    numero = 1
    segundo_numero = 3
    tercer_numero = 10
    resultado = sexadecimal_a_decimal(numero, segundo_numero, tercer_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == 3790, "El resultado no es el esperado"
    
def test_decimal_a_sexadecimal():
    """Caso de prueba de la función decimal_a_sexadecimal"""
    numero = 3790
    resultado = decimal_a_sexadecimal(numero)
    assert isinstance(resultado[0], int), "El resultado debe ser un número entero"
    assert isinstance(resultado[1], int), "El resultado debe ser un número entero"
    assert isinstance(resultado[2], int), "El resultado debe ser un número entero"
    assert resultado == (1, 3, 10), "El resultado no es el esperado"
