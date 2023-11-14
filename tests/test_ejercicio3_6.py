import pytest
from src.ejercicio3_6 import failedAsigPrinter

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      (["Mates", "Lengua", "Inglés", "Historia"], [3.5, 9, 10, 10], "Has de repetir Mates ya que has sacado un 3.5."),
      (["Matemáticas", "Biología", "Francés"], [7, 9, 4.5], "Has de repetir Francés ya que has sacado un 4.5."),
      (["Programación", "Lenguaje de Marcas", "Sistemas"], [8, 0, 8], "Has de repetir Lenguaje de Marcas ya que has sacado un 0.")
    ] 
)
def test_failedAsigPrinter_params(input_n1, input_n2, expected):
    assert failedAsigPrinter(input_n1, input_n2) == expected