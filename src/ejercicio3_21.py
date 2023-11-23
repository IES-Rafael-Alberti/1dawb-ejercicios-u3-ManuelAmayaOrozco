"""
Ejercicio 3.2.8
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá
las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción>
separados por comas. El programa debe crear un diccionario con las palabras y sus
traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla
palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""


def dicEspanglish():
    fin = False
    dic = {}
    while (fin != True):
        palabs = input("Introduce una palabra y su traducción al inglés de la siguiente manera (<palabra>:<traducción>) o introduce '0' para finalizar:")
        if (palabs == "0"):
            fin = True
        else:
            palabs = palabs.split(":")
            dic.setdefault(palabs[0],palabs[1])
    print(dic)
    return dic


def tradFrase(dic: dict):
    sent = ""
    frase = input("Dime una frase que quieras traducir: ")
    frase = frase.split(" ")
    for word in frase:
        sent += dic.get(word, word) + " "
    return sent[:-1]


def main():
    dic = dicEspanglish()
    print(tradFrase(dic))
    
    
if __name__ == "__main__":
    main()
                