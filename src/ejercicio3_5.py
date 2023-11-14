"""
Ejercicio 3.1.5
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por
pantalla en orden inverso separados por comas.
"""

def inverNumList(numer_list: list):
    """Inverses any given list, reading it backwards from how it was before.
    
    Parameters
    ----------
    numer_list : list
        The list that is provided.
        
    Returns
    -------
    numer_list : list
        The list, now in reverse.
    """
    
    
    numer_list = numer_list[::-1]
    return numer_list


def main():
    numerlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(inverNumList(numerlist))
    
    
if __name__ == "__main__":
    main()