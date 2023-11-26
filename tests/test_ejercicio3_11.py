import pytest
from src.ejercicio3_11 import producto_vectorial

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      ((1, 2, 3), (-1, 0, 2), (-1, 0, 6)),
      ((8, 3, 0), (1, 3, 6), (8, 9, 0)),
      ((-2, 3, 9), (4, 7, 2), (-8, 21, 18))
    ] 
)
def test_producto_vectorial_params(input_n1, input_n2, expected):
    assert producto_vectorial(input_n1, input_n2) == expected