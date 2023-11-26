"""
Ejercicio 3.1.7
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que
ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
"""


def alphDestroyer(alphabet: list):
    """DESTROYS any letters of the provided list that are in a position that is a multiple of 3
    
    Parameters
    ----------
    alphabet : list
        The provided list
        
    Returns
    -------
    alphabet : list
        The list, now with some of its letters destroyed.
    """
    
    
    for i in range(len(alphabet), 1, -1):
        if ((i % 3) == 0):
            alphabet.pop(i - 1)
    return alphabet


def main():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(alphDestroyer(alphabet))
    

if __name__ == "__main__":
    main()