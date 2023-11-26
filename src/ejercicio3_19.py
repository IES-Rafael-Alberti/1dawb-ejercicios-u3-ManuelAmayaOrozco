"""
Ejercicio 3.2.6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una
persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al
usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""


def personalData():
    seguir = False
    datos = {}
    while (seguir != True):
        catdat = input("Introduce una categoría de datos personales (O introduce '0' si no quieres introducir nada más): ")
        if (catdat == "0"):
            seguir = True
        else:
            dat = input("Introduce tu dato personal correspondiente de la categoría introducida: ")
            datos.setdefault(catdat,dat)
            print(datos)
    return datos
    
    
def main():
    print(personalData())
    
    
if __name__ == "__main__":
    main()