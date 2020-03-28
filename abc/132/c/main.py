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
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7

def inp(): return int(sys.stdin.readline())
 
def inp_list(): return list(map(int, sys.stdin.readline().split()))

N = inp()
dd = inp_list()

dd_sorted = sorted(dd)

border_l = dd_sorted[N // 2 - 1]
border_r = dd_sorted[N // 2]
if border_l == border_r:
    print(0)
else:
    print(border_r - border_l)
