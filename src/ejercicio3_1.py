"""
Ejercicio 3.1.1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""

def asigListMaker():
    """Lets you write a list of subjects until the user types in a "0", then returns the newly made list
    
    Returns
    -------
    asig_list : list
        List of subjects typed in by the user.
    """
    
    asig_list = []
    asig = ""
    pos = 0
    asig = input("Escribe una clase para añadir a la lista. (Escribe 0 para dejar de añadir clases): ")
    while(asig != "0"):
        asig_list.append(asig)
        pos += 1
        asig = enterAsig()
    return asig_list


def enterAsig():
    """Lets you type in the class you want to input for the list.
    
    Returns
    -------
    asig : str
        Subject you want to add to your list.
    """
    asig = input("Escribe una clase para añadir a la lista: ")
    return asig


def readListAsig(asig_list: list):
    """Reads the list of subjects that is provided by creating a string with the list.
    
    Parameters
    ----------
    asig_list : list
        The provided list of subjects to be turned into a string and read by the function.
        
    Returns
    -------
    res : str
        The resulting string to be read out.
    """
    res = ""
    for asig in asig_list:
        res += asig + ", "
    res = res[:-2] + "."
    return res


def main():
    asiglist = asigListMaker()
    print(readListAsig(asiglist))
    
    
if __name__ == "__main__":
    main()