"""
Ejercicio 3.1.4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los
almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
6 numeros del 1-49 y 1 número de reintegro 0-9, que no se repitan.
"""


def numLotLista():
    """Lets you write 6 lottery numbers and one reintegrate number, then orders the lottery numbers
    from smallest to largest.
    
    Returns
    -------
    The ordered list with the reintegrate number at the end of it.
    """
    
    
    try:
        numer_list = []
        pos = 0
        while (pos != 6):
            num = recibNumLot(numer_list)
            numer_list.append(num)
            pos += 1
        numer_list = orderNumList(numer_list)
        num = recibNumRei(numer_list)
        numer_list.append(num)
        return "El conjunto de números de loteria final es {numer_list}.".format(numer_list = numer_list)
    except ValueError:
        return "**ERROR** Valor introducido incorrecto."
    except NameError:
        return "**ERROR** Valor ya introducido en la lista."


def recibNumLot(numer_list : list):
    """Lets you type in the lottery number you want to input for the list.
    
    Parameters
    ----------
    numer_list : list
        The currently made list, used to ensure that the added number does not repeat itself.
    
    Returns
    -------
    num : int
        The lottery number you want to add to your list.
    """
    
    
    num = int(input("Dime el número de la loteria a introducir: "))
    if (num < 1 or num > 49 or type(num) != int):
        raise ValueError
    elif (num in numer_list):
        raise NameError("Numero En Lista")
    return num
    
    
def recibNumRei():
    """Lets you type in the reintegrate number you want to input at the end of the list.
    
    Returns
    -------
    num : int
        The reintegrate number you want to add to the end of your list.
    """
    
    
    num = int(input("Dime el número de reintegro a introducir: "))
    if (num < 0 or num > 9 or type(num) != int):
        raise ValueError
    return num


def orderNumList(numer_list: list):
    """Sets the order of the given list of numbers from smallest to largest.
    
    Parameters
    ----------
    numer_list : list
        The array to be ordered correctly by the function.
        
    Returns
    -------
    numer_list : list
        The same list from before, now properly ordered by the function.
    """
    
    
    total = len(numer_list) - 1
    
    for i in range(1, len(numer_list)):
        for j in range(0, total):
            if (numer_list[j] > numer_list[j+1]):
                tmp = numer_list[j]
                numer_list[j] = numer_list[j+1]
                numer_list[j+1] = tmp
        
        total -= 1
    return numer_list


def main():
    print(numLotLista())
    
    
if __name__ == "__main__":
    main()