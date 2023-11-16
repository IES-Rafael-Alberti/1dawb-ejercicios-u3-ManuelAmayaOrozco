import pytest
from src.ejercicio3_8 import palindromeDetector

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      ("eevee", "Es un palíndromo."),
      ("hola", "No es un palíndromo."),
      ("aña", "Es un palíndromo.")
    ] 
)
def test_palindromeDetector_params(input_n1, expected):
    assert palindromeDetector(input_n1) == expected