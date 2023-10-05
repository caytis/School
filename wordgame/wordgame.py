# import itertools.groupby, random.choice, random.shuffle, collections.Counter
import itertools
import random
import collections

def start(*args, **kwargs):
    with open("wordgame/words.txt") as file:
        words = file.readlines()
        for i in range(len(words)):     # Start at 0? i - 1?
            words[i] = words[i].strip()
    while True:
        inp = input("Enter the range of word lengths (low,high):")
        inp.strip()
        low = 0
        high = 0
        rang = inp.split(",")
        if rang[0] == "q":
            break
        if len(rang) != 2:
            "Invalid input. Try again."
            continue
        low = int(rang[0])
        high = int(rang[1])
        if args:
            word = kwargs
            found = search(kwargs, words, low, high)
        else:
            word = pick(words, high)
            found = search(word, words, low, high)
        check(found, word)

def pick(words, length):
    while True:
        word = random.choice(words)
        if len(word) == length:
            return word

def search(it, words, low, high):
    itsplit = collections.Counter(it)
    fits = list(words)
    for word in words:
        splits = collections.Counter(word)
        splits.subtract(itsplit)
        splits = +splits
        if splits.total() > 0 or len(word) < low or len(word) > high: # or word == it
            fits.remove(word)
    fits = sorted(fits, key=len)
    lengths = itertools.groupby(fits, lambda x : len(x)) # lambda? TODO
    return lengths
                

def check(founder, it):
    final = list()
    found = list()
    temp = list()
    i = 0
    for length, group in founder:
        temp.append(list(group))
        found.append(list())
    for line in temp:
        for word in line:
            final.append(word)
            found[i].append(str("-" * len(word)))
        i += 1
    donee = list(final)
    while True:
        wordlyst = list(it)
        random.shuffle(wordlyst)
        wordd = str(wordlyst).strip("[]").replace("'", "").replace(",", "").replace(" ", "")
        print(wordd + ":\n\n")
        for group in found:
            print(group)
            print()
        inp = input("\nEnter a guess: ")
        if inp == "q":
            done(final)
            break
        isit = False
        allfound = False
        for group in temp:
            if inp in group: # key?
                isit = True
                if donee[final.index(inp)] != True:
                    print("Correct!\n")
                    found[temp.index(group)][group.index(inp)] = inp
                    donee[final.index(inp)] = True
                else:
                    print("Already found.\n")
                    break
        i = 0
        allfound = True
        for word in final:
            if donee[i] != True:
                allfound = False
            i += 1
        if allfound == True:
            done(final)
            break
                
        if isit == False and allfound == False:
            print("Sorry. Try again\n")
        continue
    
def done(words):
    print(words)

def main():
    start()

if __name__ == '__main__':
    main()
