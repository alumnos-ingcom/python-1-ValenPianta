################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio11 import es_multiplo
"""
Este es el test correspondiente al archivo 'ejercicio11.py'
"""

def test_es_multiplo_true():
    """Caso de prueba para valores verdaderos de la función es_multiplo"""
    numero = 6
    segundo_numero = 2
    resultado = es_multiplo(numero, segundo_numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is True, "Se esperaba True"
    
def test_es_multiplo_false():
    """Caso de prueba para valores falsos de la función es_multiplo"""
    numero = 7
    segundo_numero = 2
    resultado = es_multiplo(numero, segundo_numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is False, "Se esperaba False"
