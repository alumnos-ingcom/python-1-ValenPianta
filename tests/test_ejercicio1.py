################
# Valentín Piantanida - @ValenPianta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import pytest

from src.ejercicio1 import convertir_a_fahrrenheit, convertir_a_centigrados

"""
Este es el test correspondiente al archivo 'ejercicio1.py'
"""

def test_convertir_a_fahrrenheit_positivos():
    """
    Este test evalua la funcion convertir_a_fahrrenheit() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    numero = 31
    resultado = convertir_a_fahrrenheit(numero)
    assert isinstance(resultado, float), "El resultado debe ser un numero tipo Float"
    assert resultado == 87.8, "El resultado no es el esperado"
    
def test_convertir_a_fahrrenheit_negativos():
    """
    Este test evalua la funcion convertir_a_fahrrenheit() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    numero = -10
    resultado = convertir_a_fahrrenheit(numero)
    assert isinstance(resultado, float), "El resultado debe ser un numero tipo Float"
    assert resultado == 14, "El resultado no es el esperado"

def test_convertir_a_centigrados_positivos():
    """
    Este test evalua la funcion convertir_a_centigrados() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    numero = 87.8
    resultado = convertir_a_centigrados(numero)
    assert isinstance(resultado, float), "El resultado debe ser un numero tipo Float"
    assert resultado == 31, "El resultado no es el esperado"
    
def test_convertir_a_centigrados_negativos():
    """
    Este test evalua la funcion convertir_a_centigrados() ingresando un valor y
    revisando que el resultado sea el numero esperado y de tipo Float
    """
    numero = -5
    resultado = convertir_a_centigrados(numero)
    assert isinstance(resultado, float), "El resultado debe ser un numero tipo Float"
    assert resultado == -20.56, "El resultado no es el esperado"