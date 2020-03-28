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

A, B, C, D = inp_list()

# (B 以下の条件を満たす自然数の個数) - (A - 1 以下の条件を満たす自然数の個数)
lcm_cd = lcm(C, D)
B_ans = B - B // C - B // D + B // lcm_cd
A1 = A - 1
A1_ans = A1 - A1 // C - A1 // D + A1 // lcm_cd
ans = B_ans - A1_ans
print(ans)
