################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio4 import suma_lenta
"""
Este es el test correspondiente al archivo 'ejercicio4.py'
"""

def test_suma_lenta_positivos():
    """Caso de prueba de la función suma_lenta para cuando
    ambos son positivos"""
    numero = 5
    segundo_numero = 3
    resultado = suma_lenta(numero, segundo_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == 8, "El resultado no es el esperado"

def test_suma_lenta_negativos():
    """Caso de prueba de la función suma_lenta para cuando
    ambos son negativos"""
    numero = -5
    segundo_numero = -3
    resultado = suma_lenta(numero, segundo_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == -8, "El resultado no es el esperado"
    
def test_suma_lenta_pos_neg():
    """Caso de prueba de la función suma_lenta para cuando el primer numero es
    positivo y el segundo negativo"""
    numero = 5
    segundo_numero = -3
    resultado = suma_lenta(numero, segundo_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == 2, "El resultado no es el esperado"
    
def test_suma_lenta_neg_pos():
    """Caso de prueba de la función suma_lenta para cuando el primer numero es
    negativo y el segundo positivo"""
    numero = -5
    segundo_numero = 3
    resultado = suma_lenta(numero, segundo_numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero"
    assert resultado == -2, "El resultado no es el esperado"