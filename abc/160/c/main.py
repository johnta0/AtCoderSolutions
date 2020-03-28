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


K, N = inp_list()
A = inp_list()

max_dist = 0
for i in range(N):
    if i == N - 1:
        max_dist = max(max_dist, A[0] + K - A[i])
    else:
        max_dist = max(max_dist, A[i + 1] - A[i])

print(K - max_dist)
