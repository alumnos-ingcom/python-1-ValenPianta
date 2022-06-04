################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio2 import signo
"""
Este es el test correspondiente al archivo 'ejercicio2.py'
"""

def test_signo_positivo():
    """Caso de prueba de la función signo para valores positivos"""
    numero = 4
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == 1, "El resultado no es el esperado"

def test_signo_negativo():
    """Caso de prueba de la función signo para valores negativos"""
    numero = -10
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == -1, "El resultado no es el esperado"
    
def test_signo_cero():
    """Caso de prueba de la función signo para valor ingresado cero"""
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == 0, "El resultado no es el esperado"
