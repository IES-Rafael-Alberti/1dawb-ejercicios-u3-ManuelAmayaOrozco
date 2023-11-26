import pytest
from src.ejercicio3_1 import readListAsig

@pytest.mark.parametrize(
    "input_n1, expected",
    [
      (["Mates", "Lengua", "Inglés", "Historia"], "Mates, Lengua, Inglés, Historia."),
      (["Matemáticas", "Biología", "Francés"], "Matemáticas, Biología, Francés."),
      (["Programación", "Lenguaje de Marcas", "Sistemas"], "Programación, Lenguaje de Marcas, Sistemas.")
    ] 
)
def test_readListAsig_params(input_n1, expected):
    assert readListAsig(input_n1) == expected