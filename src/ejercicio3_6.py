"""
Ejercicio 3.1.6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en
cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe
mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

from src.ejercicio3_1 import enterAsig
from src.ejercicio3_3 import asigListMakerScore, enterScore


def failedAsigPrinter(asig_list: list, note_list: list):
    """Checks the provided score list for any failed subjects (below 5) and makes a new list out
    of them along with a new list for the failed subjects in question, then prints them out one by one.
    
    Parameters
    ----------
    asig_list : list
        The provided list of subjects.
    note_list : list
        The provided list of notes, in the same order as their respective subjects.
        
    Returns
    ------
    The final iteration of the printing loop.
    """
    
    count = 0
    asigrep_list = []
    noterep_list = []
    
    for i in range(0, len(asig_list)):
        note_temp = note_list[i]
        if (note_temp < 5):
            asigrep_list.append(asig_list[i])
            noterep_list.append(note_list[i])
            
    while (count < (len(asigrep_list)-1)):
        if (float(note_list[count]) == int(note_list[count])):
            noterep_list[count] = int(noterep_list[count])
        else:
            noterep_list[count] = round(noterep_list[count], 2)
        print("Has de repetir {asigrep} ya que has sacado un {notarep}.".format(asigrep = asigrep_list[count], notarep = noterep_list[count]))
        count += 1
        
    if (float(noterep_list[count]) == int(noterep_list[count])):
        noterep_list[count] = int(noterep_list[count])
    else:
        noterep_list[count] = round(noterep_list[count], 2)
    return "Has de repetir {asigrep} ya que has sacado un {notarep}.".format(asigrep = asigrep_list[count], notarep = noterep_list[count])


def main():
    asiglist, notelist = asigListMakerScore()
    print(failedAsigPrinter(asiglist, notelist))
    
    
if __name__ == "__main__":
    main()