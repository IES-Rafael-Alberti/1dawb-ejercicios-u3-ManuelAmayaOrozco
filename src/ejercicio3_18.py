"""
Ejercicio 3.2.5
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los
créditos de cada asignatura en el formato "<asignatura> tiene <créditos> créditos", donde
<asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final
debe mostrar también el número total de créditos del curso.
"""


def creditAsignaturas():
    tot = 0
    seguir = False
    asignaturas = {}
    while(seguir != True):
        asig,credit = pedirAsigCredit()
        asignaturas.setdefault(asig, credit)
        seguirval = input("¿Quieres seguir añadiendo asignaturas? (Sí para continuar): ")
        if (seguirval != "Sí"):
            seguir = True
    for asigna,cred in asignaturas.items():
        print("{asigna} tiene {cred} créditos.".format(asigna = asigna, cred = cred))
        tot += cred
    return "El total de créditos de todas las asignaturas es de {tot}".format(tot = tot)


def pedirAsigCredit():
    try:
        asig = input("Introduce la asignatura deseada: ")
        if (type(asig) != str):
            raise ValueError
        cred = int(input("Introduce la cantidad de créditos que vale la asignatura: "))
        if (type(cred) != int):
            raise ValueError
        return asig, cred
    except ValueError:
        return "**ERROR** Valor introducido incorrecto."
    
    
def main():
    print(creditAsignaturas())
    
    
if __name__ == "__main__":
    main()