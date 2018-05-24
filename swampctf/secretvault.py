from hashlib import sha256

# https://stackoverflow.com/questions/11747254/python-brute-force-algorithm
from itertools import chain, product
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))


# a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

a = "smaug123"

b = bruteforce(a, 8)

cnt = 0
for p in b:
  if sha256(p.encode('ascii')).hexdigest == "40f5d109272941b79fdf078a0e41477227a9b4047ca068fff6566104302169ce":
    print p
    break
  cnt += 1
  print cnt