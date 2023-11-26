import pytest
from src.ejercicio3_9 import vowelCounter

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      ("eevee", [0, 4, 0, 0, 0]),
      ("hola", [1, 0, 0, 1, 0]),
      ("aña", [2, 0, 0, 0, 0])
    ] 
)
def test_vowelCounter_params(input_n1, expected):
    assert vowelCounter(input_n1) == expected