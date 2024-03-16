import math
import sys

p = int(sys.argv[1])
q = int(sys.argv[2])
n = p * q
on = (p-1) * (q-1)

gcd = 0
e = 1
d = 1
for i in range(int(on / 2), 0, -1):
    gcd = math.gcd(i, on + 1)
    if gcd > 1:
        e = gcd
        d = int((on + 1) / e)
        break

print(f'Public key: ({e}, {n}). Private key: ({d}, {n}).')
