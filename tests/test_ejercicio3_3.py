import pytest
from src.ejercicio3_3 import subjNotePrinter

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
      (["Mates", "Lengua", "Inglés", "Historia"], [6.5, 9, 10, 10], "En Historia has sacado 10."),
      (["Matemáticas", "Biología", "Francés"], [7, 9, 5.5], "En Francés has sacado 5.5."),
      (["Programación", "Lenguaje de Marcas", "Sistemas"], [8, 6, 8], "En Sistemas has sacado 8.")
    ] 
)
def test_subjNotePrinter_params(input_n1, input_n2, expected):
    assert subjNotePrinter(input_n1, input_n2) == expected