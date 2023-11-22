"""
Ejercicio 3.2.3
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte
al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de
kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Fruta     Precio
Plátano   1.35
Manzana   0.80
Pera      0.85
Naranja   0.70
"""


def Fruteria():
    try:
        tot = 0
        
        fruteria = {"Plátano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}
        
        selec = input("Elige una fruta a comprar (Plátano, Manzana, Pera, Naranja): ")
        
        kilo = int(input("¿Cuántos kilos quieres comprar?: "))
        if (type(kilo) != int):
            raise ValueError
        
        if (selec == "Plátano"):
            tot = (fruteria["Plátano"] * kilo)
        elif (selec == "Manzana"):
            tot = (fruteria["Manzana"] * kilo)
        elif (selec == "Pera"):
            tot = (fruteria["Pera"] * kilo)
        elif (selec == "Naranja"):
            tot = (fruteria["Naranja"] * kilo)
        else:
            raise NameError
        return "El precio total es de {tot}€.".format(tot = round(tot,2))
    except ValueError:
        return "**ERROR** Valor no válido."
    except NameError:
        return "**ERROR** La fruta no introducida no es válida."
    
    
def main():
    print(Fruteria())
    
    
if __name__ == "__main__":
    main()