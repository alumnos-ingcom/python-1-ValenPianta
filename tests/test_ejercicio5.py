################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio5 import division_lenta
"""
Este es el test correspondiente al archivo 'ejercicio5.py'
"""

def test_division_lenta():
    """Caso de prueba de la función division_lenta"""
    numero = 8
    segundo_numero = 3
    resultado = division_lenta(numero, segundo_numero)
    assert isinstance(resultado[0], int), "El cociente debe ser un número entero"
    assert isinstance(resultado[1], int), "El resto debe ser un número entero"
    assert resultado[0] == 2, "El resultado no es el esperado"
    assert resultado[1] == 2, "El resultado no es el esperado"