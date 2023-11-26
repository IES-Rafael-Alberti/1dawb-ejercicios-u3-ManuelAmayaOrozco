import pytest
from src.ejercicio3_12 import matrixProdCalc

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      (((1, 2, 3), (4, 5, 6)), ((-1, 0), (0, 1), (1, 1)), ((2, 5), (2, 11))),
      (((3, 2, 1), (4, 6, 5)), ((-2, 0), (1, 1), (1, 0)), ((-3, 2), (3, 6))),
      (((1, 1, 1), (5, 6, 5)), ((-2, 0), (1, 1), (1, 0)), ((0, 1), (1, 6)))
    ] 
)
def test_matrixProdCalc_params(input_n1, input_n2, expected):
    assert matrixProdCalc(input_n1, input_n2) == expected