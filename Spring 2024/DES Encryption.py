import sys

plainM = "0123456789ABCDEF" #sys.argv[1]
plainK = "133457799BBCDFF1" #sys.argv[2]

plainM = bin(int(plainM, 16))[2:].zfill(64)
binK = bin(int(plainK, 16))[2:].zfill(64)

pc1 = [
    56, 48, 40, 32, 24, 16, 8,
    0, 57, 49, 41, 33, 25, 17,
    9, 1, 58, 50, 42, 34, 26,
    18, 10, 2, 59, 51, 43, 35,
    62, 54, 46, 38, 30, 22, 14,
    6, 61, 53, 45, 37, 29, 21,
    13, 5, 60, 52, 44, 36, 28,
    20, 12, 4, 27, 19, 11, 3
]

Kplus = [binK[i] for i in pc1]

firstC = "".join(Kplus[:28])
firstD = "".join(Kplus[28:])

shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

Cs = [firstC]
Ds = [firstD]

for i in range(16):
    Cs.append("".join(Cs[i-1][shifts[i-1]:] + Cs[i-1][:shifts[i-1]]))
    Ds.append("".join(Ds[i-1][shifts[i-1]:] + Ds[i-1][:shifts[i-1]]))

newKs = [Cs[i] + Ds[i] for i in range(16)]

pc2 = [
    13, 16, 10, 23, 0, 4,
    2, 27, 14, 5, 20, 9,
    22, 18, 11, 3, 25, 7,
    15, 6, 26, 19, 12, 1,
    40, 51, 30, 36, 46, 54,
    29, 39, 50, 44, 32, 47,
    43, 48, 38, 55, 33, 52,
    45, 41, 49, 35, 28, 31
]

allKs = ["".join([newKs[i][j] for j in pc2]) for i in range(16)]

ip = [
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8, 0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6
]

ipedM = "".join([plainM[i] for i in ip])

firstL = ipedM[:32]
firstR = ipedM[32:]

edible = [
    31, 0, 1, 2, 3, 4,
    3, 4, 5, 6, 7, 8,
    7, 8, 9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31, 0
]

Ls = [format(int(firstL, 16), '032b')]
Rs = [format(int(firstR, 16), '032b')]

for i in range(16):
    newR = "".join([Rs[i-1][x] for x in edible])
    erK = int(Rs[i-1], 2) ^ int(allKs[i], 2)
    endingR = format(int(Ls[i-1], 2) ^ erK, '032b')
    endingL = Rs[-1]
    Rs.append(endingR)
    Ls.append(endingL)

ip_1 = [39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
    32, 0, 40, 8, 48, 16, 56, 24]

print(Rs)
