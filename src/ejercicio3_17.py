"""
Ejercicio 3.2.4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la
misma fecha en formato "dd de <mes> de aaaa" donde <mes> es el nombre del mes.
"""


def askDate():
    meses = {"01":"Enero", "02":"Febrero", "03":"Marzo", "04":"Abril", "05":"Mayo", "06":"Junio", "07":"Julio", "08":"Agosto", "09":"Septiembre", "10":"Octubre", "11":"Noviembre", "12":"Diciembre"}
    fecha = input("Introduce la fecha en formato dd/mm/aaaa: ")
    fecha = (fecha).split("/")
    return "{dia} de {mes} de {año}.".format(dia = fecha[0], mes = meses[fecha[1]], año = fecha[2])


def main():
    print(askDate())
    
    
if __name__ == "__main__":
    main()