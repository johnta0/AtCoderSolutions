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

N, K = inp_list()
ans = 0
for k in range(K, N + 2):
    # M => 和の最大値, m => 和の最小値, k について和としてありえるものの個数は M - m + 1
    M = ( N * (N + 1) // 2 - (N - k) * (N + 1 - k) // 2 )
    m = k * (k - 1) // 2
    ans += (M - m + 1)

print(ans % mod)
