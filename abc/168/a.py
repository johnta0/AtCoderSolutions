import sys
from collections import deque
import bisect
import math
import itertools
from queue import deque
from math import gcd

INF = float('inf')
mod = 10**9+7
eps = 10**-7


def inp(): return int(sys.stdin.readline())


def inp_list(): return list(map(int, sys.stdin.readline().split()))


def lcm(x, y): return (x * y) // gcd(x, y)

N = inp()
r = -1
if 0 < N < 10:
    r = N
else:
    r = int(str(N)[-1])

if r in [2, 4, 5, 7, 9]:
    print('hon')
elif r in [0, 1, 6, 8]:
    print('pon')
else:
    print('bon')

