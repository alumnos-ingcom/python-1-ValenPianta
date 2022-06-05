################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio3 import compara
"""
Este es el test correspondiente al archivo 'ejercicio3.py'
"""

def test_compara_mayor():
    """Caso de prueba de la función compara para cuando
    el primero es mayor que el segundo"""
    numero = 5
    segundo_numero = 3
    resultado = compara(numero, segundo_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == 1, "El resultado no es el esperado"

def test_compara_menor():
    """Caso de prueba de la función compara para cuando
    el primero es menor que el segundo"""
    numero = 2
    segundo_numero = 8
    resultado = compara(numero, segundo_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == -1, "El resultado no es el esperado"
    
def test_compara_iguales():
    """Caso de prueba de la función compara para cuando
    ambos numeros son iguales"""
    numero = 7
    segundo_numero = 7
    resultado = compara(numero, segundo_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == 0, "El resultado no es el esperado"
