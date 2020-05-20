import sys
# from collections import deque
# import bisect
# import math
# import itertools
# from queue import deque
# from math import gcd

INF = float('inf')
mod = 10**9+7
eps = 10**-7


def inp(): return int(sys.stdin.readline())


def inp_list(): return list(map(int, sys.stdin.readline().split()))


def lcm(x, y): return (x * y) // gcd(x, y)


N, M = inp_list()
X = inp_list()
X.sort()
# print(X)

if N >= M:
    print(0)
    exit()

d = [X[i + 1] - X[i] for i in range(M - 1)]
# for i in range(M - 1): d.append(X[i + 1] - X[i])
# print(d)
d.sort()
ans = sum(d[: M - 1 - (N - 1)])
# ans = 0
# for i in range(M - 1 -  (N - 1)):
    # ans += d[i]
print(ans)
