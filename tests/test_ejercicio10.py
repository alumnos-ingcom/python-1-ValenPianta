################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio10 import es_palindromo
"""
Este es el test correspondiente al archivo 'ejercicio10.py'
"""

def test_es_palindromo_true():
    """Caso de prueba de la función es_palindromo en el que la entrada es palíndromo"""
    texto = "neuquen"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is True, "Se esperaba True"
    
def test_es_palindromo_false():
    """Caso de prueba de la función es_palindromo en el que la entrada no es palíndromo"""
    texto = "nonstop"
    resultado = es_palindromo(texto)
    assert isinstance(resultado, bool), "El resultado debe ser True o False"
    assert resultado is False, "Se esperaba False"
