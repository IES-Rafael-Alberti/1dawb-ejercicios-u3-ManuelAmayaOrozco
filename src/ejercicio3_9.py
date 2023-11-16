"""
Ejercicio 3.1.9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces
que contiene cada vocal.
"""


from src.ejercicio3_8 import receiveWord


def vowelCounter(word: str):
    """Counts all the different vowels in a word or phrase, and then shows a list composed of 
    all the total vowesl of each type.
    
    Parameters
    ----------
    word : str
        The word that has been provided.
        
    Returns
    -------
    list_appear : list
        The list of all the total vowels that have been counted in the word.
    """
    
    
    list_appear = []
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        appear = 0
        for letter in word:
            if (letter == vowel):
                appear += 1
        print("La vocal {vowel} aparece {appear} veces en la palabra.".format(vowel = vowel, appear = str(appear)))
        list_appear.append(appear)
    return list_appear
        
        
        
def main():
    word = receiveWord()
    print(vowelCounter(word))
    
    
if __name__ == "__main__":
    main()