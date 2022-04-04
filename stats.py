import sys
import glob
import random

LETTERS_VALUE = [
    ("A", 1),
    ("B", 1),
    ("C", 1),
    ("D", 1),
    ("E", 1),
    ("F", 1),
    ("G", 1),
    ("H", 1),
    ("I", 1),
    ("J", 1),
    ("K", 1),
    ("L", 1),
    ("M", 1),
    ("N", 1),
    ("O", 1),
    ("P", 1),
    ("Q", 1),
    ("R", 1),
    ("S", 1),
    ("T", 1),
    ("U", 1),
    ("V", 1),
    ("W", 1),
    ("X", 1),
    ("Y", 1),
    ("Z", 1)]

def help(nb):
    print("USAGE")
    print("\tanagram [letters]",end="\n\n")
    print("Va afficher les anagrammes possibles avec ces lettres")
    exit(nb)

def getContentFile():
    file = open(glob.glob("index.json")[0], 'r')
    content = file.read()
    return content.replace("\"", "").split(",")

def stats(arg, words, tab):
    if len(sys.argv) != 2:
        exit(1)
    count = 0
    nb = 0
    letters = 0
    for word in words:
        letters += len(word)
        count += word.count(arg)
        if arg in word:
            nb += 1
    # print("pourcentage sur le total de lettres: ", 100*count/letters)
    # print("pourcentage de mot comprenant " + arg + ": ", 100*nb/len(words), end="\n\n")
    tab.append([arg, 100*nb/len(words)])
    return tab

def main():
    tab = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    words = getContentFile()
    for letter in alphabet:
        tab = stats(letter, words, tab)
    print (sorted(tab, key = lambda x: x[1]))
    return 0

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exited")
        exit(0)
    # except IndexError:
    #     print("IndexError: list index out of range")
    #     exit(1)


# E A I R S N T O U L C M D P G B F H Z V Q Y X J K W