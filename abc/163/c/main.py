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


N = inp()
A = [0] + inp_list()

ans_list = [0 for _ in range(N)]
# print(ans_list)
for a in A:
    ans_list[a - 1] += 1
    # print(ans_list)
ans_list[-1] = 0

for ans in ans_list:
    print(ans)
