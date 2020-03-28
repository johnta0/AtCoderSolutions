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
ans = [0] * (N - 1)
ans[0] = N

for i in range(1, N - 1):
    ans[i] = N - (i + 1)

shortcut = Y - X
for k in range(1, N - 2):
    if sum(ans[:k]) == N * (N + 1) // 2:
        ans[k:] = [0] * (N - 1 - k + 1)
        break
    if k < shortcut:
        ans[k] += 2
    elif k == shortcut:
        ans[k] -= 1
        ans[k] += 2
    else: # k > shortcut
        if X > 1 and Y < N:
           ans[k] += 1 


ans[-1] = N * (N + 1) // 2 - sum(ans[:-1])

for a in ans:
    print(a)
