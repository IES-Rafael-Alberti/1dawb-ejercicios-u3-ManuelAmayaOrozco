import pytest
from src.ejercicio3_13 import calcMed, calcTypDev

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      ((1, 2, 3, 4, 5), 3),
      ((6, 7, 8, 9, 10), 8),
      ((11, 13, 15, 17, 19), 15)
    ] 
)
def test_calcMed_params(input_n1, expected):
    assert calcMed(input_n1) == expected
    
    
@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      ((1, 2, 3, 4, 5), 3, 1.4142135623730951),
      ((6, 7, 8, 9, 10), 8, 1.4142135623730951),
      ((11, 13, 15, 17, 19), 15, 2.8284271247461903)
    ] 
)
def test_calcTypDev_params(input_n1, input_n2, expected):
    assert calcTypDev(input_n1, input_n2) == expected