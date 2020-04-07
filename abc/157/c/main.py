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


N, M = inp_list()
s = [0] * M
c = [0] * M
for i in range(M): s[i], c[i] = inp_list()

if M == 0:
    if N == 1:
        print(0)
        exit()
    else:
        print(10 ** (N - 1))
        exit()


# N 桁の整数 10 ** (N - 1) ~ 10 ** N - 1 を全探索
for i in range(10 ** (N - 1) - 1, 10 ** N):
    if N != 1 and i == 10 ** (N - 1) - 1: continue
    i_str = str(i)
    for m in range(M):
        if i_str[s[m] - 1] != str(c[m]):
            break
        if m == M - 1:
            print(i)
            exit()
print(-1)
