import sys
import glob
import random

BAD_LETTERS = []

def help(nb):
    """
    Print the help
    :param nb: the number of the help
    """
    print("USAGE")
    print("\ttusmo",end="\n\n")
    print("refait le jeu motus mais en python")
    exit(nb)


def getContentFile():
    """
    Return the content of the file
    :return: the content of the file
    """
    file = open(glob.glob("index.json")[0], 'r')
    content = file.read()
    return content.replace("\"", "").split(",")


def getNCharsLength(words, n):
    """
    Return a list of words with the same length as n
    :param words: the list of words
    :param n: the length of the words
    :return: a list of words with the same length as n
    """
    res = []
    for word in words:
        if len(word) == n and checkAlpha(word):
            res.append(word)
    return res


def checkAlpha(word):
    """
    Return True if the word is made of letters
    :param word: the word to check
    :return: True if the word is made of letters
    """
    for letter in word:
        if letter.isalpha() == False:
            return False
    return True

def objectsWithCountOfEachLetters(words):
    """
    Return a list of objects with the count of each letter
    :param words: the list of words
    :return: a list of objects with the count of each letter
    """
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    for letter in allLetters:
        res.append({letter: sum([x.count(letter) for x in words if letter in x])})
    return res


def ponderatesWords(words, allLettersOccurrences):
    """
    Print all words that have the same letters as the guess
    :param words: the list of words
    :param allLettersOccurrences: the list of all letters occurrences
    """
    allLetters = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    for word in words:
        ponderate = 0
        for letter in allLetters:
            if letter in word:
                ponderate += allLettersOccurrences[allLetters.index(letter)][letter]
        ponderate += countNumberOfWordSameLetterSamePlace(words, word)
        res.append({'word': word, 'ponderate': ponderate})
    res.sort(key=lambda x: x['ponderate'], reverse=True)
    print(*res[:5], sep="\n")
    return res


def countNumberOfWordSameLetterSamePlace(words, guess):
    """
    Return the number of words that have the same letters as the guess
    :param words: the list of words
    :param guess: the guess
    return: the number of words that have the same letters as the guess"""
    res = 0
    for word in words:
        for i in range (0, len(word)):
            if guess[i] == word[i]:
                res += 1
    return res


def haveGoodLetters(word, guess):
    """
    Return a string with the same length as the word
    :param word: the word to check
    :param guess: the guess
    :return: a string with the same length as the word
    """
    res = ''
    for i in range (0, len(word)):
        if guess[i] in word:
            if word[i] == guess[i]:
                print(guess[i], end='')
                res += guess[i]
                word = word[:i] + "0" + word[i+1:]
            else:
                print('?', end='')
                res += '?'
        else:
            print('_', end='')
            res += '_'
            BAD_LETTERS.append(guess[i])
    print()
    return res


def returnGoodPotentialWord(word, res):
    """
    Return True if the word has the same letters as the guess
    :param word: the word to check
    :param res: the result of the haveGoodLetters function
    return: True if the word has the same letters as the guess
    """
    for i in range (0, len(word)):
        if res[i] == '_' or res[i] == '?':
            if word[i] in BAD_LETTERS:
                return False
            pass
        elif word[i] != res[i]:
            return False
    return True


def printWordsThatHaveSameLetters(res, words):
    """
    Print all words that have the same letters as the guess
    :param res: the result of the haveGoodLetters function
    :param words: the list of words
    """
    print('Mot potentiels:')
    potentials = []
    for word in words:
        if returnGoodPotentialWord(word, res):
            potentials.append(word)
    ponderatesWords(potentials, objectsWithCountOfEachLetters(potentials))


def main():
    """
    Main function
    """
    words = getContentFile()
    five = getNCharsLength(words, 5)
    print("5 lettres")
    randomWord = random.choice(five)
    obj = objectsWithCountOfEachLetters(five)
    guess = input("Quel est le mot ? ")
    while guess != randomWord:
        if guess not in five:
            print("Mauvais mot")
            guess = input()
        res = haveGoodLetters(randomWord, guess)
        printWordsThatHaveSameLetters(res, five)
        guess = input()
    print("Bravo !")
    print("Le mot était:", randomWord)
    return 0


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exited")
        exit(0)
    except IndexError:
        print("IndexError: list index out of range")
        exit(1)

# UNIT TESTS #

def test_checkAlpha():
    """
    Test the checkAlpha function
    """
    assert checkAlpha("abc") == True
    assert checkAlpha("abc1") == False
    assert checkAlpha("abc1a") == False
    assert checkAlpha("abc1a1") == False
    assert checkAlpha("abc1a1a") == False

def test_getNCharsLength():
    """
    Test the getNCharsLength function
    """
    assert getNCharsLength(["abc", "abcd", "abcde", "abcdef", "abcdefg"], 3) == ["abc"]
    assert getNCharsLength(["abc", "abcd", "abcde", "abcdef", "abcdefg"], 4) == ["abcd"]
    assert getNCharsLength(["abc", "abcd", "abcde", "abcdef", "abcdefg"], 5) == ["abcde"]
    assert getNCharsLength(["abc", "abcd", "abcde", "abcdef", "abcdefg"], 6) == ["abcdef"]
    assert getNCharsLength(["abc", "abcd", "abcde", "abcdef", "abcdefg"], 7) == ["abcdefg"]
    assert getNCharsLength(["abc", "abcd", "abcde", "abcdef", "abcdefg"], 8) == []

def test_objectsWithCountOfEachLetters():
    """
    Test the objectsWithCountOfEachLetters function
    """
    assert objectsWithCountOfEachLetters(["abc", "abcd", "abcde", "abcdef", "abcdefg"]) == [{'a': 5}, {'b': 5}, {'c': 5}, {'d': 4}, {'e': 3}, {'f': 2}, {'g': 1}, {'h': 0}, {'i': 0}, {'j': 0}, {'k': 0}, {'l': 0}, {'m': 0}, {'n': 0}, {'o': 0}, {'p': 0}, {'q': 0}, {'r': 0}, {'s': 0}, {'t': 0}, {'u': 0}, {'v': 0}, {'w': 0}, {'x': 0}, {'y': 0}, {'z': 0}]
