"""
Ejercicio 3.1.8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""


def palindromeDetector(word: str):
    """Detects if a given word is a palindrome by turning them into lists and checking if the reversed
    version is the same as the normal one.
    
    Parameters
    ----------
    word : str
        The word that is given, to check if its a palindrome.
    
    Returns
    -------
    The result of whether its a palindrome or not.
    """
    
    
    rev_word = word
    word = list(word)
    rev_word = list(rev_word)
    rev_word.reverse()
    if (word == rev_word):
        return "Es un palíndromo."
    else:
        return "No es un palíndromo."
    
    
def receiveWord():
    """Lets you input a word of your choosing.
    
    Returns
    -------
    word : str
        The word you inputted previously.
    """
    
    
    word = input("Introduce una palabra: ")
    return word


def main():
    word = receiveWord()
    print(palindromeDetector(word))
    
    
if __name__ == "__main__":
    main()