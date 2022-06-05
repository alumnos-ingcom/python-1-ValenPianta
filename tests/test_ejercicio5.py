################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio5 import division_lenta
"""
Este es el test correspondiente al archivo 'ejercicio5.py'
"""

def test_division_lenta_positivos():
    """Caso de prueba de la función division_lenta para numeros positivos"""
    numero = 8
    segundo_numero = 3
    resultado = division_lenta(numero, segundo_numero)
    assert isinstance(resultado[0], int), "El cociente debe ser un número entero"
    assert isinstance(resultado[1], int), "El resto debe ser un número entero"
    assert resultado == (2, 2), "El resultado no es el esperado"

def test_division_lenta_negativos():
    """Caso de prueba de la función division_lenta para numeros negativos"""
    numero = -9
    segundo_numero = -4
    resultado = division_lenta(numero, segundo_numero)
    assert isinstance(resultado[0], int), "El cociente debe ser un número entero"
    assert isinstance(resultado[1], int), "El resto debe ser un número entero"
    assert resultado == (2, -1), "El resultado no es el esperado"

def test_division_lenta_positivo_negativo():
    """Caso de prueba de la función division_lenta para dividendo positivo y
    divisor negativo"""
    numero = 13
    segundo_numero = -4
    resultado = division_lenta(numero, segundo_numero)
    assert isinstance(resultado[0], int), "El cociente debe ser un número entero"
    assert isinstance(resultado[1], int), "El resto debe ser un número entero"
    assert resultado == (-3, 1), "El resultado no es el esperado"

def test_division_lenta_negativo_positivo():
    """Caso de prueba de la función division_lenta para dividendo positivo y
    divisor negativo"""
    numero = -20
    segundo_numero = 3
    resultado = division_lenta(numero, segundo_numero)
    assert isinstance(resultado[0], int), "El cociente debe ser un número entero"
    assert isinstance(resultado[1], int), "El resto debe ser un número entero"
    assert resultado == (-6, -2), "El resultado no es el esperado"
    