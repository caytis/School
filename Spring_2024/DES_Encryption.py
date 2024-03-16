import sys

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

shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

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

sBoxes = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
]

P = [
    15, 6, 19, 20,
    28, 11, 27, 16,
    0, 14, 22, 25,
    4, 17, 30, 9,
    1, 7, 23, 13,
    31, 26, 2, 8,
    18, 12, 29, 5,
    21, 10, 3, 24
]

fp = [
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
    32, 0, 40, 8, 48, 16, 56, 24
]

def encrypt(plainM, plainK):
    binM = format(int(plainM, 16), '064b')
    binK = format(int(plainK, 16), '064b')

    Kplus = [binK[i] for i in pc1]

    firstC = "".join(Kplus[:28])
    firstD = "".join(Kplus[28:])

    Cs = [firstC]
    Ds = [firstD]

    for i in range(16):
        Cs.append("".join(Cs[i][shifts[i]:] + Cs[i][:shifts[i]]))
        Ds.append("".join(Ds[i][shifts[i]:] + Ds[i][:shifts[i]]))

    newKs = [Cs[i+1] + Ds[i+1] for i in range(16)]

    allKs = ["".join(newKs[i][x] for x in pc2) for i in range(16)]

    # print(f"Part 1: {allKs}")

    ipedM = "".join([binM[i] for i in ip])

    firstL = ipedM[:32]
    firstR = ipedM[32:]

    Ls = [firstL]
    Rs = [firstR]

    for i in range(16):
        exR = "".join([Rs[i][x] for x in edible])
        exRK = format(int(exR, 2) ^ int(allKs[i], 2), '048b')
        Bs = [exRK[x*6:x*6+6] for x in range(8)]
        Boutside = [int(Bs[x][0] + Bs[x][-1], 2) for x in range(8)]
        Binside = [int(Bs[x][1:5], 2) for x in range(8)]
        Sss = "".join([format(sBoxes[x][Boutside[x]][Binside[x]], '04b') for x in range(8)])
        Pdone = "".join([Sss[x] for x in P])
        endingR = int(Ls[i], 2) ^ int(Pdone, 2)

        Rs.append(format(endingR, '032b'))
        Ls.append(Rs[i])

    lastRL = Rs[-1] + Ls[-1]
    C = format(int("".join([lastRL[x] for x in fp]), 2), "016X")

    print(f"Part 2: {C}")

def decrypt(plainC, plainK):
    binC = format(int(plainC, 16), '064b')
    binK = format(int(plainK, 16), '064b')
    Kplus = [binK[i] for i in pc1]

    firstC = "".join(Kplus[:28])
    firstD = "".join(Kplus[28:])

    Cs = [firstC]
    Ds = [firstD]

    for i in range(16):
        Cs.append("".join(Cs[i][shifts[i]:] + Cs[i][:shifts[i]]))
        Ds.append("".join(Ds[i][shifts[i]:] + Ds[i][:shifts[i]]))

    newKs = [Cs[i+1] + Ds[i+1] for i in range(16)]
    allKs = ["".join(newKs[i][x] for x in pc2) for i in range(16)]
    
    unfp = "".join([binC[f] for f in ip]) ###
    
    Ls = [unfp[32:]]
    Rs = [unfp[:32]]

    for i in range(16):
        Rs.append(Ls[i])
        exR = "".join([Rs[i+1][x] for x in edible])
        exRK = format(int(exR, 2) ^ int(allKs[-i-1], 2), '048b')
        Bs = [exRK[x*6:x*6+6] for x in range(8)]
        Boutside = [int(Bs[x][0] + Bs[x][-1], 2) for x in range(8)]
        Binside = [int(Bs[x][1:5], 2) for x in range(8)]
        Sss = "".join([format(sBoxes[x][Boutside[x]][Binside[x]], '04b') for x in range(8)])
        Pdone = "".join([Sss[x] for x in P])
        endingR = int(Rs[i], 2) ^ int(Pdone, 2)

        Ls.append(format(endingR, '032b'))
    
    firstL = Ls[-1]
    firstR = Rs[-1]
    ipedM = firstL + firstR
    M = "".join([ipedM[i] for i in fp])
    print(f"Original Message Hex is {format(int(M, 2), '016X')}")


def main():
    plainMorC = sys.argv[1]
    # plainM = "0123456789ABCDEF"
    # plainC = "85E813540F0AB405"
    plainK = sys.argv[2] # 133457799BBCDFF1
    # encrypt(plainMorC, plainK)
    decrypt(plainMorC, plainK)

if __name__ == "__main__":
    main()
    