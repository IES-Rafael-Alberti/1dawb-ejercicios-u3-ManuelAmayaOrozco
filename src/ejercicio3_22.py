"""
Ejercicio 3.2.9
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las
facturas se almacenarán en un diccionario donde la clave de cada factura será el número de
factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir
una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se
preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una
factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada
operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la
cantidad pendiente de cobro.
"""


def modFacturas():
    facturas = {}
    cobrad = 0
    pend = 0
    rep = ""
    while (rep != "T"):
        if (rep == "A"):
            clave = input("Introduce el número de la factura: ")
            cost = float(input("Introduce el coste de la factura: "))
            facturas[clave] = cost
            pend += cost
        elif (rep == "P"):
            clave = input("Introduce el número de la factura a pagar: ")
            cost = facturas.pop(clave, 0)
            cobrad += cost
            pend -= cost
        print("Redcaudado: {cobrad}".format(cobrad = cobrad))
        print("Pendiente de cobro: {pend}".format(pend = pend))
        rep = input("Añadir factura (A).\nPagar factura (P).\nTerminar modificaciones (T).\n¿Que desea hacer?: ")
    return "Finalizado."


def main():
    print(modFacturas())
    
    
if __name__ == "__main__":
    main()