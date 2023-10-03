import itertools.groupby, random.choice, random.shuffle

def start():
    inp = ""
    with open("words.txt") as file:
        words = file.readlines()
        for i in words:     # Start at 0? i - 1?
            words[i] = words[i].strip()
        while inp != "q":
            inp = input("Enter the range of word lengths (low,high):")
            inp.strip()
            rang = inp.split(",")
            low = rang[0]
            high = rang[1]
            word = pick(words, high)
            found = search(word, words, low, high)
            write(found)

def pick(words, length):
    words = random.shuffle(words)
    for word in words:
        if len(word) == length:
            pass

def search(it, words, low, high):
    pass

def write(found):
    pass

def main():
    pass

if __name__ == '__main__':
    main()
