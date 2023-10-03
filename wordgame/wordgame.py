import itertools.groupby, random.choice, random.shuffle

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
            check(found)
            # check()
            # continue

def pick(words, length):
    words = random.shuffle(words)
    for word in words:
        if len(word) == length:
            return word
    print("No words in this range found")

def search(it, words, low, high):
    fits = words
    for letter in it:
        for word in fits:
            if not (len(word) >= low and len(word) <= high and letter in word):
                fits.remove(word)
    lengths = itertools.groupby(words, lambda x : len(x)) # lambda?
    return lengths
                

def check(found):
    pass

def main():
    pass

if __name__ == '__main__':
    main()
