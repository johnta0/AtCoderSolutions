n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

def factorial(n):
    if n < 2:
        return 1
    ret = 1
    for i in range(2, n + 1):
        ret *= i
    return ret

import itertools
seq = list(map(lambda x: x + 1, list(range(n))))
ptr = list(itertools.permutations(seq))

print(abs( ptr.index(p) - ptr.index(q) ))
