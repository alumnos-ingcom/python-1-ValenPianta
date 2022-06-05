################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio8 import es_primo
"""
Este es el test correspondiente al archivo 'ejercicio8.py'
"""

def test_es_primo_true():
    """Caso de prueba de la función es_primo en que el numero ingresado es primo"""
    numero = 11
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is True, "Se esperaba True"

def test_es_primo_false():
    """Caso de prueba de la función es_primo en que el numero ingresado no es primo"""
    numero = 14
    resultado = es_primo(numero)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is False, "Se esperaba True"