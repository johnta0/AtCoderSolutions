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

dp = [INF] * N
dp[0] = 0 # initial condition
# 計算量: O(NK)
for i in range(N - 1):
    for j in range(i + 1, i + K + 1):
        if j > N - 1: break
        dp[j] = min(dp[j], dp[i] + abs(h[i] - h[j])) # recurrence formula
    
print(dp[N - 1])
