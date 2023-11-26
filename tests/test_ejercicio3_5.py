import pytest
from src.ejercicio3_5 import inverNumList

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      ([6, 45, 34, 23, 44, 8], [8, 44, 23, 34, 45, 6]),
      ([7, 33, 22, 14, 40, 28], [28, 40, 14, 22, 33, 7]),
      ([1, 22, 44, 5, 23, 4], [4, 23, 5, 44, 22, 1])
    ] 
)
def test_inverNumList_params(input_n1, expected):
    assert inverNumList(input_n1) == expected