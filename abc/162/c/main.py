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
from math import gcd

sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10 ** -7

def inp(): return int(sys.stdin.readline())
 
def inp_list(): return list(map(int, sys.stdin.readline().split()))

def lcm(x, y): return (x * y) // gcd(x, y)


K = inp()

def gcd_3(x, y, z):
    return gcd(gcd(x, y), z)

dic = {} # key: (i, j, k), el: gcd(i, j, k)
ans = 0
# for i in range(1, K + 1):
#     for j in range(i, K + 1):
#         # tmp = gcd(i, j)
#         for k in range(j, K + 1):
#             # a = gcd(tmp, k)
#             # a = gcd(gcd(i, j), k)
#             a = gcd_3(i, j, k)
#             if i == j == k:
#                 ans += a
#             elif i == j or j == k:
#                 ans += a * 3
#             else:
#                 ans += a * 3 * 2

# 全探索
for i in range(1, K + 1):
    for j in range(1, K + 1):
        for k in range(1, K + 1):
            ans += gcd_3(i, j, k)
print(ans)
