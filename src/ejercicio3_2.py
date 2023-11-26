"""
Ejercicio 3.1.2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje 'Yo estudio
<asignatura>', donde <asignatura> es sobre cada una de las asignaturas de la lista.
"""


from src.ejercicio3_1 import asigListMaker, enterAsig


def iStudyPrinter(asig_list: list):
    """Reads all the subjects on a list starting with the phrase "Yo estudio <asignatura>." where 'asignatura' is a subject from the list.
    
    Parameters
    ----------
    asig_list : list
        The list that will be used by the function.
    
    Returns
    -------
    The final iteration of the loop.
    """
    
    
    count = 0
    while (count < (len(asig_list)-1)):
        print("Yo estudio {asig_listc}.".format(asig_listc = asig_list[count]))
        count += 1
    return "Yo estudio {asig_listc}.".format(asig_listc = asig_list[count])

def main():
    asiglist = asigListMaker()
    print(iStudyPrinter(asiglist))
    
    
if __name__ == "__main__":
    main()