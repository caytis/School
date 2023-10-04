# import itertools.groupby, random.choice, random.shuffle, collections.Counter
import itertools
import random
import collections

def start():
    # inp = ""
    with open("wordgame/words.txt") as file:
        words = file.readlines()
        for i in range(len(words)):     # Start at 0? i - 1?
            words[i] = words[i].strip()
        while True:
            # inp = input("Enter the range of word lengths (low,high):")
            inp = "3,6"
            inp.strip()
            rang = inp.split(",")
            if len(rang) != 2:
                "Invalid input. Try again."
                continue
            if rang[0] == "q": # Fix
                # TODO: smn
                pass
            low = int(rang[0])
            high = int(rang[1])
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
    itsplit = collections.Counter(it)
    # wordsplit = collections.Counter(words)
    fits = list(words)
    for word in words:
        splits = collections.Counter(word)
        splits.subtract(itsplit)
        splits = +splits
        if splits.total() > 0 or len(word) < low or len(word) > high: # or word == it
            fits.remove(word)
    # for word in fits:
    #     if word not in it: # does this work?
    #         fits.remove(word)
    lengths = list(itertools.groupby(fits, lambda x : len(x))) # lambda?
    # for group, iterr in groupby(lengths):
    #     lengths[group] = dict(iterr)
    # itertools.
    return lengths
                

def check(founder, it):
    final = list()
    found = list()
    for length in founder:
        found.append(list(length[1]))
        for word in found:
            word = {word : str("-" * len(word))}
            final.append(word)
    
    while True:
        print(random.shuffle(it) + ":\n")
        allfound = False # TODO
        for length in found:
            print(word.keys())
        inp = input("\nEnter a guess:")
        if inp == "q":
            done(final)
            break
        isit = False
        for length in found:
            if inp in length: # key?
                isit = True
                print("Correct!\n")
                length[inp] = inp
                break
        if isit == False:
            print("Sorry. Try again\n")
        continue
    
def done(words):
    print(words)

def main():
    start()

if __name__ == '__main__':
    main()
