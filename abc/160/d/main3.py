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


N, X, Y = inp_list()

"""
    XY間のショートカット経路を使う場合と使わない場合の距離をそれぞれ計算して、
    その小さい方が最短経路。
"""

ans = [0] * N
for i in range(N):
    for j in range(i + 1, N):
        min_dist = min(j - i, abs(X - i - 1) + 1 + abs(Y - j - 1))
        ans[min_dist] += 1

for i in range(1, N):
    print(ans[i])
