from collections import  deque
import sys
import bisect
# import math
import itertools
from queue import deque
# from math import gcd

INF = float('inf')
mod = 10**9+7
eps = 10**-7

def inp(): return int(sys.stdin.readline())
 
def inp_list(): return list(map(int, sys.stdin.readline().split()))

# def lcm(x, y): return (x * y) // gcd(x, y)

N = inp()
A = [0 for _ in range(N)]
xx = [[] for _ in range(N)]
yy = [[] for _ in range(N)]

for i in range(N):
    A[i] = inp()
    for _ in range(A[i]):
        x, y = inp_list()
        xx[i].append(x)
        yy[i].append(y)

# ↑ inputs
# ↓ main process

# {0, 1, ..., N-1} の集合の bit 全探索
ans = 0
for bit in range(1 << N):
    """
        例： bit == 10 のとき、2進数では 001010 
            右から人 1, 2, ..., 6 と対応させる。
    """
    is_inconsistent = False
    # 整数 bit を２進数表示し、右から 1/0 を True/False に置換
    is_honest = [(bit >> i) & 1 for i in range(N)]
    for i in range(N):
        if not is_honest[i]: continue
        for (x, y) in zip(xx[i], yy[i]):
            if is_honest[x - 1] != y:
                is_inconsistent = True # 矛盾
    if not is_inconsistent:
        ans = max(ans, sum(is_honest))
print(ans)
