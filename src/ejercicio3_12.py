"""
Ejercicio 3.1.12
Escribir un programa que almacene las matrices A=(123456) y B=(-100111) en una lista y
muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas
anidadas, representando cada vector fila en una lista.
"""


def matrixProdCalc(A: tuple, B: tuple):
    """Calculates the product of two different matrixes.
    
    Parameters
    ----------
    A : tuple
        The first matrix.
    B : tuple
        The second matrix.
        
    Returns
    -------
    result : tuple
        The resulting matrix.
    """
    
    
    result = [[0, 0], [0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    for i in range(len(result)):
        result[i] = tuple(result[i])
    return tuple(result)


def main():
    A = ((1, 2, 3), (4, 5, 6))
    B = ((-1, 0), (0, 1), (1, 1))
    print(matrixProdCalc(A, B))
    

if __name__ == "__main__":
    main()