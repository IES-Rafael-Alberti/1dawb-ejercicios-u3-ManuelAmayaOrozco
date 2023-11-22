"""
Ejercicio 3.2.7
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa
debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida
terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el
siguiente formato
Lista de la compra
Artículo 1          Precio
Artículo 2          Precio
Artículo 3          Precio
...                 ...
Total               Coste
"""


def cestaCompra():
    fin = False
    tot = 0
    cesta = {}
    while (fin != True):
        prod = input("¿Qué quieres comprar? (Introduce '0' para dejar de comprar): ")
        if (prod == "0"):
            fin = True
        else:
            price = float(input("¿Cuál es el precio del producto?: "))
            cesta.setdefault(prod,price)
            tot += price
            print("Cesta actual: {cesta}".format(cesta = cesta))
    print("Cesta final: {cesta}".format(cesta = cesta))
    return "El precio final de la compra es de {tot}€.".format(tot = round(tot,2))


def main():
    print(cestaCompra())
    
    
if __name__ == "__main__":
    main()