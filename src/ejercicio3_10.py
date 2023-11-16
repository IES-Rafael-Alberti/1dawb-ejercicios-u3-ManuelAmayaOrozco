"""
Ejercicio 3.1.10
Escribir un programa que almacene en una lista los siguientes precios: [50, 75, 46, 22, 80,
65, 8] y muestre por pantalla el menor y el mayor de los precios.
"""


def priceMaxMin(price_list: list):
    """Shows the smallest and largest price withina  given list.
    
    Parameters
    ----------
    price_list : list
        The list of prices that will be used.
        
    Returns
    -------
    The resulting smallest and largest numbers from that list.
    """
    
    
    count = 0
    minim = maxim = price_list[0]
    while (count < len(price_list)):
        if (price_list[count] < minim):
            minim = price_list[count]
        elif (price_list[count] > maxim):
            maxim = price_list[count]
        count += 1
    print("El menor precio de la lista es {minim}.".format(minim = minim))
    return "El mayor precio de la lista es {maxim}.".format(maxim = maxim)


def main():
    price_list = [50, 75, 46, 22, 80, 65, 8]
    print(priceMaxMin(price_list))
    
    
if __name__ == "__main__":
    main()