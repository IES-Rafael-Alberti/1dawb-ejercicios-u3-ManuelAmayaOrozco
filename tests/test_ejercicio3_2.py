import pytest
from src.ejercicio3_2 import iStudyPrinter

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (["Mates", "Lengua", "Inglés", "Historia"], "Yo estudio Historia."),
      (["Matemáticas", "Biología", "Francés"], "Yo estudio Francés."),
      (["Programación", "Lenguaje de Marcas", "Sistemas"], "Yo estudio Sistemas.")
    ] 
)
def test_iStudyPrinter_params(input_n1, expected):
    assert iStudyPrinter(input_n1) == expected