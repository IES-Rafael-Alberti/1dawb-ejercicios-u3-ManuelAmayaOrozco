import pytest
from src.ejercicio3_7 import alphDestroyer

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], ['a', 'b', 'd', 'e', 'g', 'h', 'j', 'k', 'm', 'n', 'o', 'p', 'r', 's', 'u', 'v', 'x', 'y'])
    ] 
)
def test_alphDestroyer_params(input_n1, expected):
    assert alphDestroyer(input_n1) == expected