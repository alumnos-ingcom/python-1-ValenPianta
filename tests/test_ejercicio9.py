################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio9 import factores_primos
"""
Este es el test correspondiente al archivo 'ejercicio9.py'
"""

def test_factores_primos():
    """Caso de prueba de la función factores_primos para un numero entero positivo"""
    numero = 34
    resultado = factores_primos(numero)
    assert isinstance(resultado, tuple), "El resultado debe ser una Tupla"
    assert resultado == (2, 17), "El resultado no es el esperado"
