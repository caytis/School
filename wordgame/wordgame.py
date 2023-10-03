# import itertools.groupby, random.choice, random.shuffle, collections.Counter
from itertools import groupby
from random import choice, shuffle
from collections import Counter

def start():
    # inp = ""
    with open("words.txt") as file:
        words = file.readlines()
        for i in words:     # Start at 0? i - 1?
            words[i] = words[i].strip()
        while True:
            inp = input("Enter the range of word lengths (low,high):")
            inp.strip()
            if inp == "q":
                break
            rang = inp.split(",")
            low = rang[0]
            high = rang[1]
            word = pick(words, high)
            found = search(word, words, low, high)
            check(found, word)
            # check()
            # continue

def pick(words, length):
    while True:
        word = random.choice(words)
        if len(word) == length:
            return word
    # print("No words in this range found")

def search(it, words, low, high):
    fits = words
    for word in fits:
        if not (len(word) >= low and len(word) <= high):
            fits.remove(word)
    for word in fits:
        if word not in it: # does this work?
            fits.remove(word)
    lengths = itertools.groupby(fits, lambda x : len(x)) # lambda?
    return lengths
                

def check(found, it):
    for length in found:
        for word in length:
            word = {word : str("'" + "-" * len(word) + "'")}
    while True:
        print(random.shuffle(it) + ":")
        for length in found:
            print(length) # need to change it to 
            
            # TODO
        
        inp = input("Enter a guess:")

def main():
    pass

if __name__ == '__main__':
    main()
