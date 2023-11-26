import pytest
from src.ejercicio3_10 import priceMaxMin

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      ([50, 75, 46, 22, 80, 65, 8], "El mayor precio de la lista es 80."),
      ([100, 34, 566, 78, 34, 5 ,99], "El mayor precio de la lista es 566."),
      ([1, 2], "El mayor precio de la lista es 2.")
    ] 
)
def test_priceMaxMin_params(input_n1, expected):
    assert priceMaxMin(input_n1) == expected