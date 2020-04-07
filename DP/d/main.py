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


N, W = inp_list()
weight = [0] * N  # np.array([0] * N)
value = [0] * N  # np.array([0] * N)
for i in range(N):
    weight[i], value[i] = inp_list()

# dp[i + 1][w] : i番目までの品物の中から重さがwを超えないように選んだときの価値の和の最大値
# dp = np.zeros((N + 1, W + 1), dtype=int)  # w = 0, 1, ..., W
dp = [[0] * N + 1]
# dp[0] = [0, 0, ..., 0]
# print(dp)

for i in range(N):
    for w in range(W + 1):
        if w < weight[i]:
            # i番目の品物を選ばない. w < weight[i] のときは weight[i] を選ぶと w を超えるので
            dp[i + 1][w] = dp[i][w]
        else:
            # i番目の品物を選ぶとき. 選ばない
            dp[i + 1][w] = max(dp[i][w], dp[i][W - weight[i]] + value[i])

# print(weight)
# print(value)
print(dp)
print(dp[N][W])
