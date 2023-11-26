import pytest
from src.ejercicio3_4 import orderNumList

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      ([6, 45, 34, 23, 44, 8], [6, 8, 23, 34, 44, 45]),
      ([7, 33, 22, 14, 40, 28], [7, 14, 22, 28, 33, 40]),
      ([1, 22, 44, 5, 23, 4], [1, 4, 5, 22, 23, 44])
    ] 
)
def test_orderNumList_params(input_n1, expected):
    assert orderNumList(input_n1) == expected