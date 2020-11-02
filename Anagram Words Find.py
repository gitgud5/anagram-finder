"""
Load file
Then take the user's word and look for anagram in the dictionary
"""
from d_load import load


def anagrams():

    word = input("Give the word to find anagram for: ")

    a = set(load("212.txt")) #load function is already defined in d_load module created in other direcory
    b = set()
    b.add(word)

    for i in a:
        if sorted(i)==sorted(word):
            b.add(i)

    return b

print(*anagrams(), sep="\n")
