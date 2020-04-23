from collections import  deque
import sys
import bisect
import math
import itertools
from queue import deque
from math import gcd

INF = float('inf')
mod = 10**9+7
eps = 10**-7

def inp(): return int(sys.stdin.readline())
 
def inp_list(): return list(map(int, sys.stdin.readline().split()))

def lcm(x, y): return (x * y) // gcd(x, y)

N, M = inp_list()
A = inp_list()

ans = N - sum(A)
if ans < 0:
    print(-1)
    exit()
print(ans)
