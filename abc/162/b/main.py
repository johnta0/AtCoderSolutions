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

n = inp()
ans = 0
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0: continue
    if i % 3 == 0: continue
    if i % 5 == 0: continue
    ans += i
print(ans)