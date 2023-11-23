"""
Ejercicio 3.3.2
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una
escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los
nombres de los alumnos de secundaria, finalizando al introducir “x”.
- Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
- Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
- Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
- Mostrar si todos los nombres de primaria están incluidos en secundaria.
"""


def pedir_alumnos(msj: str) -> list:
    print(msj)
    alumnos = []
    alumno = ""
    cont = 0
    while alumno != "x":
        cont += 1
        alumno = input("{cont} => ".format(cont = cont)).strip()
        if alumno.lower() != "x":
            alumnos.append(alumno.title())
            
    return alumnos


def main():
    alumnos_primaria = pedir_alumnos("Introduzca los alumnos de Primaria ('x' para terminar): ")
    alumnos_secundaria = pedir_alumnos("Introduzca los alumnos de Secundaria ('x' para terminar): ")
    
    conj_primaria = {alumnos_primaria}
    conj_secundaria = {alumnos_secundaria}
    print(conj_primaria | conj_secundaria)
    print(conj_primaria.union(conj_secundaria))
    
    print(conj_primaria & conj_secundaria)
    
    print(conj_primaria - conj_secundaria)
    
    print(conj_primaria <= conj_secundaria)
