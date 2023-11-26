"""
Ejercicio 3.2.2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde
en un diccionario. Después debe mostrar por pantalla el mensaje "<nombre> tiene <edad> años,
vive en <dirección> y su número de teléfono es <teléfono>."
"""


def lectDatos():
    datos = {}
    
    nom = input("Introduce tu nombre: ")
    datos["Nombre"] = nom
    
    edad = input("Introduce tu edad: ")
    datos["Edad"] = edad
    
    direc = input("Introduce tu dirección: ")
    datos["Direccion"] = direc
    
    tfno = input("Introduce tu teléfono: ")
    datos["Telefono"] = tfno
    
    return "{Nombre} tiene {Edad} años, vive en {Direccion} y su número de teléfono es {Telefono}.".format(Nombre = datos["Nombre"], Edad = datos["Edad"], Direccion = datos["Direccion"], Telefono = datos["Telefono"])


def main():
    print(lectDatos())
    
    
if __name__ == "__main__":
    main()