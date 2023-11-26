"""
Ejercicio 3.1.3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en
cada asignatura, y después las muestre por pantalla con el mensaje 'En <asignatura> has
sacado <nota>.' donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada
una de las correspondientes notas introducidas por el usuario.
"""


from src.ejercicio3_1 import enterAsig


def asigListMakerScore():
    """Lets you write a list of subjects, as well as their respective scores, until the user
    types in a "0", then returns the newly made list
    
    Returns
    -------
    asig_list : list
        List of subjects typed in by the user.
    note_list : list
        List of scores typed by the user, in the same order as their respective subjects.
    """
    
    
    asig_list = []
    note_list = []
    asig = ""
    pos = 0
    asig = input("Escribe una clase para añadir a la lista. (Escribe 0 para dejar de añadir clases): ")
    note = float(input("Escribe la nota que has sacado en la clase introducida: "))
    while(asig != "0"):
        asig_list.append(asig)
        note_list.append(note)
        pos += 1
        asig = enterAsig()
        if (asig != "0"):
            note = enterScore()
    return asig_list, note_list


def enterScore():
    """Lets you type in the score you want to input for the list.
    
    Returns
    -------
    note : float
        Score you want to add to your list.
    """
    
    
    note = float(input("Escribe la nota que has sacado en la clase introducida: "))
    return note


def subjNotePrinter(asig_list: list, note_list: list):
    """Reads all the subjects and their scores from two lists, starting with the phrase "En
    <asignatura> has sacado <nota>." where 'asignatura' is a subject and 'nota' is its respective
    score.
    
    Parameters
    ----------
    asig_list : list
        The list of subjects that will be used by the function.
    note_list : list
        The list of scores that will be used by the function.
    
    Returns
    -------
    The final iteration of the loop.
    """
    
    
    count = 0
    while (count < (len(asig_list)-1)):
        if (float(note_list[count]) == int(note_list[count])):
            note_list[count] = int(note_list[count])
        else:
            note_list[count] = round(note_list[count], 2)
        print("En {asig_listc} has sacado {note_listc}.".format(asig_listc = asig_list[count], note_listc = note_list[count]))
        count += 1
    if (float(note_list[count]) == int(note_list[count])):
        note_list[count] = int(note_list[count])
    else:
        note_list[count] = round(note_list[count], 2)
    return "En {asig_listc} has sacado {note_listc}.".format(asig_listc = asig_list[count], note_listc = note_list[count])


def main():
    asiglist, notelist = asigListMakerScore()
    print(subjNotePrinter(asiglist, notelist))
    
    
if __name__ == "__main__":
    main()