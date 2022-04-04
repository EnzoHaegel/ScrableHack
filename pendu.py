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

def value(word):
    res = 0
    for letters in LETTERS_VALUE:
        if letters[0] in word.upper():
            res += letters[1]
    print(res)
    return (res)

def main():
    fausses = []
    bonnes = ''
    words = getContentFile()
    word = words[random.randint(0, len(words))]
    blank = ['_']*len(word)
    print("".join(blank))
    while sorted(bonnes) != sorted(word) and len(fausses) < 5:
        s = input()
        if len(s) == 1 and s in word:
            bonnes += s
            for i in range(0, len(word)):
                if s == word[i]:
                    blank[i] = s
            print("\n--------------------------\n")
            print('   ' + "".join(blank) + "\t\tMauvaise lettres: ", fausses)
        elif len(s) == 1:
            fausses.append(s)
            print("\n"+'-'*20+"\n")
            print('   ' + "".join(blank) + "\t\tMauvaise lettres: ", fausses)
    print("la réponse était: " + word)
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