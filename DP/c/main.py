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
# a = np.zeros((N, 3), dtype=int)
a = [0] * N

for i in range(N):
    a[i] = inp_list()

# dp[i + 1][j]: i日目までの活動で、i日目に活動 j (0: A, 1: B, 2:C) を選んだときの i + 1 日目の幸福の最大値
# dp = np.zeros((N + 1, 3), dtype=int)
dp = [[0] * 3 for _ in range(N + 1)]
for i in range(N):
    for j in range(3): # i 日目の活動
        for k in range(3): # i + 1 日目の活動
            if j == k: continue
            dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + a[i][k])

ans = 0
for i in range(3):
    ans = max(ans, dp[N][i]) # N 日目を終了したときの幸福度 => dp[N][] (N + 1 番目)

# print(a)
# print(dp)
print(ans)
