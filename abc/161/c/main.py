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


N, K = inp_list()

mod = N % K
sho = N // K

if mod == 0:
    print(0)
else:
    ans = min(abs(sho * K - N), abs((sho + 1) * K - N))
    print(ans)

