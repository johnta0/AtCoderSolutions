from collections import defaultdict, deque
import sys
import heapq
import bisect
import math
import itertools
import string
import queue
import copy
import time
# import numpy as np
from fractions import gcd

sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7


def inp(): return int(sys.stdin.readline())


def inp_list(): return list(map(int, sys.stdin.readline().split()))


def lcm(x, y): return (x * y) // gcd(x, y)


N = inp()
S = input()

"""
    Conditions:
        1. S[i] \ne S[j] and S[j] \ne S[k] and S[k] \ne S[i]
        2. j - i \ne k - j
"""

r = S.count('R')
g = S.count('G')
b = S.count('B')
# 条件1を満たす組は rgb 個。それから「条件1を満たしてかつ条件 2 を満たさない」組を引く。条件を満たさないもののほうが多い。


cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        k = j + (j - i) # => k - j == j - i
        if k > N - 1: break
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            cnt += 1

print(r * g * b - cnt)
