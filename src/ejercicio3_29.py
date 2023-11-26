"""
Ejercicio 3.3.5
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

Crea un conjunto 'pares' que contenga los números pares del conjunto 'numeros'.
Crea un conjunto 'multiplos_de_tres' que contenga los números que son múltiplos de tres
del conjunto 'numeros'.
Encuentra la intersección entre los conjuntos 'pares' y 'multiplos_de_tres' y guárdala en un
conjunto llamado 'pares_y_multiplos_de_tres'.
"""


def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    pares = set()
    multiplos_de_tres = set()
    
    for i in numeros:
        if ((i % 2) == 0):
            pares.add(i)
        if ((i % 3) == 0):
            multiplos_de_tres.add(i)
    
    pares_y_multiplos_de_tres = set(pares & multiplos_de_tres)
    
    print("Números: {numeros}".format(numeros = numeros))
    print("Pares: {pares}".format(pares = pares))
    print("Múltiplos de tres: {multiplos_de_tres}".format(multiplos_de_tres = multiplos_de_tres))
    print("Intersección pares y múltiplos de tres: {pares_y_multiplos_de_tres}".format(pares_y_multiplos_de_tres = pares_y_multiplos_de_tres))
    
    
if __name__ == "__main__":
    main()