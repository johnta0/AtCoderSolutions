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
import numpy as np
from fractions import gcd

sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7

def inp(): return int(sys.stdin.readline())
 
def inp_list(): return list(map(int, sys.stdin.readline().split()))

def lcm(x, y): return (x * y) // gcd(x, y)


N, K = inp_list()
h = inp_list()
h = np.array(h)

dp = np.array([10 ** 5] * N)
dp[0] = 0

for i in range(N - 1):
    dp[i + 1 : i + K + 1] = np.minimum(dp[i + 1 : i + K + 1], dp[i] + abs(h[i + 1 : i + K + 1] - h[i]))

# print(dp)
print(dp[-1])
