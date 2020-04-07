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


def base_10_to_n(x, n):
    if (int(x/n)):
        return base_10_to_n(int(x / n), n)+str(x % n)
    return str(x % n)


N, K = inp_list()
n_base_k = base_10_to_n(N, K)
print(len(n_base_k))
