"""
Ejercicio 3.2.1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$',
'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la
divisa no está en el diccionario.
"""

def elecDivisa():
    try:
        divisas = {'Euro':'€', 'Dollar':'$','Yen':'¥'}
        res = input("Dime una divisa entre las siguientes elecciones (Euro, Dollar, Yen): ")
        if (res == "Euro"):
            return "Has elegido {eur}".format(eur = divisas["Euro"])
        elif (res == "Dollar"):
            return "Has elegido {dol}".format(dol = divisas["Dollar"])
        elif (res == "Yen"):
            return "Has elegido {yen}".format(yen = divisas["Yen"])
        else:
            raise ValueError
    except ValueError:
        return "**ERROR** Valor introducido incorrecto."
    
    
def main():
    print(elecDivisa())
    
    
if __name__ == "__main__":
    main()