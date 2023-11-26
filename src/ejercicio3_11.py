"""
Ejercicio 3.1.11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre
por pantalla su producto escalar.
"""


def producto_vectorial(v1: tuple, v2: tuple) -> tuple:
    """Multiplies two vectors together and hands out the resulting vector.
    
    Parameters
    ----------
    v1 : tuple
        The first vector.
    v2 : tuple
        The second vector.
        
    Returns
    -------
    v3 : tuple
        The resulting vector after multiplying the previous two.    
    """
    
    
    return tuple(v1[i] * v2[i] for i in range(len(v1)))
    
    
    """
    Manera con for: 
    t3 = ()
    
    for i in range(len(v1)):
        t3.append(v1[i] * v2[i])
    
    return t3
    """
    
    
    """
    Manera con while:
    l3 = []
    
    cont = 0
    while(cont < len(v1)):
        l3.append(v1[cont] * v2[cont])
        cont += 1
        
    return tuple(l3)        
    """


def main():
    v1 = (1, 2, 3)
    v2 = (-1, 0, 2)
    
    v3 = producto_vectorial(v1, v2)
    
    print(v3)
    
    #v3 = (-1, 0, 6)
    
    
if __name__ == "__main__":
    main()