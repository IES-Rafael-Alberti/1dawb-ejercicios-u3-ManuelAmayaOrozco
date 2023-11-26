"""
Ejercicio 3.1.13
Escribir un programa que pregunte por una muestra de números, separados por comas, los
guarde en una lista y muestre por pantalla su media y desviación típica.
"""


def calcMed(num_tup: tuple):
    """Calculates the average from a given list of numbers.
    
    Parameters
    ----------
    num_tup : tuple
        The tuple of numbers that will be used.
        
    Returns
    -------
    med : float
        The average from the given list.
    """
    
    
    sum = 0
    for i in num_tup:
        sum += i
    med = sum / len(num_tup)
    return med


def calcTypDev(num_tup: tuple, med: float):
    """Calculates the typical deviation from a given tuple of numbers and a given average.
    
    Parameters
    ----------
    num_tup : tuple
        The tuple of numbers that will be used.
    med : float
        The given average that will be used.
    
    Returns
    -------
    typdev : float
        The resulting typical deviation.
    """
    
    
    sumsquared = 0
    for i in num_tup:
        sumsquared += i**2
    typdev = (sumsquared / len(num_tup) - med**2)**(1 / 2)
    return typdev


def receiveNum(amount: int):
    """Allows you to input an amount of numbers and makes a tuple out of them.
    
    Parameters
    ----------
    amount : int
        The amount of numbers you wish for your tuple to have.
        
    Returns
    -------
    num_list : tuple
        The resulting list, turned into a tuple.
    """
    
    
    num_list = []
    while (amount != 0):
        num = int(input("Dime un número para añadir a la lista: "))
        num_list.append(num)
        amount -= 1
    return tuple(num_list)
    
    
def main():
    amount = int(input("¿Cuántos números deseas introducir?: "))
    num_list = receiveNum(amount)
    med = calcMed(num_list)
    typdev = calcTypDev(num_list, med)
    print("La media es {med} y la desviación típica es {typdev}.".format(med = med, typdev = typdev))
    

if __name__ == "__main__":
    main()